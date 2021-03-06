from app.main import db
from app.main.model.user import User
from app.main.model.list import List
from app.main.model.mylist import Mylist
from sqlalchemy import exc,case
from datetime import datetime
from app.main.util import get_current_time
from app.main.service import remove_unnecessary_elements,get_next_page,get_per_page,get_filter_condition_by_searchword,get_recommended_enddate
from ..service.complete_list_service import get_my_completelist
from ..service.todo_list_service import get_my_todolist

def get_reclist(uid,selection):
    '''유저의 할일 리스트 취득'''
    # 추천일정에서 표시할 일정중 나의 완료일정과 할일일정을 제외함(검색조건) 
    if uid:
        # 제외할 나의 완료일정과 할일일정을 디비에서 가져옴
        my_complete_list=[ x.postId for x in get_my_completelist(uid)['my_completelist']]
        my_todo_list=[ x.postId for x in get_my_todolist(uid)['my_todolist']]
        my_list_not_me = List.query.filter(List.writerUid==uid).with_entities(List.postId).all()
        my_list_not_me_list = [y[0]for y in my_list_not_me]
        # 완료일정,할일일정,작성자가 포함된 게시글을 제외한 데이터
        myList = my_complete_list+my_todo_list + my_list_not_me_list
    else:
        # 제외할 나의 완료일정과 할일일정을 로컬스토리지에서 가져옴
        my_complete_list=[x['postId'] for x in selection['myCompletelist']]
        my_todo_list=[x['postId'] for x in selection['myTodolist']]
        myList = my_complete_list+my_todo_list

    # SQL의 검색조건 취득
    filters = remove_unnecessary_elements(selection)
    # 나의 할일일정과 완료일정제외된 추천일정 취득
    my_reclist_query = List.query.filter_by(**filters).filter(~List.postId.in_(myList))

    # 추천 일정 취득
    if selection['stayStatus'] == '1' and selection['entryDate'] is not None:
    # 체류중인 상태에 입국날짜를 선택한 경우 나의 입국날짜에 근접한 추천일정을 반환
        return get_reclist_orderby_entry_date(selection,my_reclist_query)
    else:
    # 일반적인 추천일정반환
        return  get_reclist_orderby(selection,my_reclist_query)


def get_reclist_orderby(selection,my_reclist_query):
    '''일반 추천일정 반환'''
    # 페이지네이션 취득
    page = get_next_page(selection) # 표시할 페이지수를 취득
    per_page =get_per_page(selection) # 한 페이지에 표시할 게시물의 수를 취득

    # 재검색시 사용하는 검색조건
    filter_searchWord = get_filter_condition_by_searchword(selection)

    # 일반 추천일정의 SQL
    my_reclist_result = my_reclist_query.\
    filter(filter_searchWord).\
    order_by(List.createdDate.desc()).\
    paginate(page,per_page,error_out=False)

    my_reclist = {} # 반환일정정보
    my_reclist['my_reclist'] = my_reclist_result.items # 추천일정
    my_reclist['has_next'] = my_reclist_result.has_next # 다음페이지 유무
    my_reclist['current_page'] = my_reclist_result.page # 현재페이지
    my_reclist['total_count'] = my_reclist_query.count() # 총 추천일정 수
    return my_reclist


def get_reclist_orderby_entry_date(selection,my_reclist_query):
    '''나의 입국날짜에 근접한 추천일정을 반환'''
    entryDate = datetime.strptime(selection['entryDate'],'%Y-%m-%d') # 나의 입국날짜
    currentDate = datetime.strptime(get_current_time().strftime('%Y-%m-%d'),'%Y-%m-%d') # 현재시간

    # 만약 나의 입국날짜가 현재시간보다 미래일 경우 일반 추천 일정반환
    if currentDate < entryDate:
        return  get_reclist_orderby(selection,my_reclist_query)
    
    # 페이지네이션 취득
    page = get_next_page(selection) # 표시할 페이지수를 취득
    per_page =get_per_page(selection) # 한 페이지에 표시할 게시물의 수를 취득
    diff = (currentDate-entryDate).days # 내 입국후 경과 일수

    # 재검색시 사용하는 검색조건
    filter_searchWord = get_filter_condition_by_searchword(selection)

    # 내 입국경과일수보다 입국경과일수가 높은 게시물을 반환하는 SQL
    my_reclist_result_order_by = my_reclist_query.\
        filter(filter_searchWord).\
        order_by(case((List.afterEntryDate >= diff, 1),else_=0).desc()).\
        paginate(page,per_page,error_out=False)

    my_reclist = {} # 반환일정정보
    my_reclist['my_reclist'] = my_reclist_result_order_by.items
    my_reclist['has_next'] = my_reclist_result_order_by.has_next
    my_reclist['current_page'] = my_reclist_result_order_by.page
    my_reclist['total_count'] = my_reclist_query.count()
    return my_reclist


def update_reclist(uid,postId):
    '''유저의 추천일정을 추가함'''
    try:
        user=User.query.filter_by(uid=uid).first()
        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            mylist = Mylist()
            mylist.myListIdRef = postId
            mylist.uid = uid
            mylist.listKind = 'todo'

            # 새로운 일정에 일정 시작일과 일정 종료일 추가
            afterEntryDate = List.query.filter_by(postId=postId).first().afterEntryDate # 게시물의 입국 경과일
            mylist.myStartDate =  get_current_time() # 추천 일정 시작일
            mylist.myEndDate = get_recommended_enddate(afterEntryDate) # 추천 일정 종료일

            db.session.add(mylist)
            db.session.commit()
                        
            response_object = {
                'status': 'success',
                'message': '추천일정을 등록했습니다'
            }
            return response_object, 201
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 등록된 일정입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '추천일정 등록중 에러가 발생하였습니다'
        }
        return response_object, 401