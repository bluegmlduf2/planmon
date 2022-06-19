from app.main import db
from app.main.model.user import User
from app.main.model.list import List
from app.main.model.mylist import Mylist
from datetime import datetime
from app.main.util import remove_unnecessary_elements,get_next_page,get_per_page,get_current_time
from ..service.complete_list_service import get_my_completelist
from ..service.todo_list_service import get_my_todolist

def get_reclist(uid,selection):
    '''유저의 할일 리스트 취득'''
    # SQL의 검색조건 취득
    filters = remove_unnecessary_elements(selection) 
    
    # 페이지네이션 취득
    page = get_next_page(selection) # 표시할 페이지수를 취득
    per_page =get_per_page(selection) # 한 페이지에 표시할 게시물의 수를 취득

    # 추천일정에서 표시할 일정중 나의 완료일정과 할일일정을 제외함(검색조건) 
    if uid:
        # 제외할 나의 완료일정과 할일일정을 디비에서 가져옴
        my_complete_list=[ x.postId for x in get_my_completelist(uid)['my_completelist']]
        my_todo_list=[ x.postId for x in get_my_todolist(uid)['my_todolist']]
        myList = my_complete_list+my_todo_list
    else:
        # 제외할 나의 완료일정과 할일일정을 로컬스토리지에서 가져옴
        my_complete_list=[x['postId'] for x in selection['myCompletelist']]
        my_todo_list=[x['postId'] for x in selection['myTodolist']]
        myList = my_complete_list+my_todo_list

    # 추천 일정 취득
    # 나의 할일일정과 완료일정제외된결과
    # 일정을 10개를 한페이지로 표시한다
    my_reclist_query = List.query.filter_by(**filters).filter(~List.postId.in_(myList)).order_by(List.createdDate.desc())
    my_reclist_result = my_reclist_query.paginate(page,per_page,error_out=False)
    my_reclist_count = my_reclist_query.count()
    my_reclist = {
        'my_reclist':my_reclist_result.items, # 추천일정
        'has_next':my_reclist_result.has_next, # 다음페이지 유무
        'current_page':my_reclist_result.page, # 현재페이지
        'total_count':my_reclist_count, # 총 추천일정 수
    }

    # 체류중인상태에서 입국후 지난 날짜의 조건이 가까운 순서로 조회
    if selection['stayStatus'] == '1' and selection['entryDate'] is not None:
        dateFormat = '%Y-%m-%d'
        entryDate = datetime.strptime(selection['entryDate'],dateFormat) # 입국날짜
        currentDate = datetime.strptime(get_current_time().strftime(dateFormat),dateFormat) # 현재시간
        # 만약 입국날짜가 현재시간보다 미래일 경우 일반 추천 일정반환
        if currentDate < entryDate:
            return my_reclist['my_reclist']
        diff = (currentDate-entryDate).days # 입국후 경과 일수
        # 사용자에게 유효한 추천일정을 상위에 표시한다
        # 아래의 로직은 일정의 인덱스 위치를 변경하는 로직
        added_item = []
        deleted_item = []
        for x in my_reclist['my_reclist']:
            # 사용자의 입국후 일자와 작성자의 입국후 일정시작 일자를 비교해서 유효한 리스트를 상위에 표시한다
            if diff > x.afterEntryDate:
                added_item.append(x)
                deleted_item.append(x)
        # 삭제한 아이템을 추천일정으로부터 삭제하기
        for x in deleted_item:
            my_reclist['my_reclist'].remove(x)
        # 변경한 순서의 리스트를 재할당 
        my_reclist['my_reclist'] = my_reclist['my_reclist']+added_item
        
    return my_reclist


def update_reclist(uid,postId):
    '''유저의 추천일정을 추가함'''
    try:
        print(postId)
        user=User.query.filter_by(uid=uid).first()
        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            mylist = Mylist()
            mylist.myListIdRef = postId
            mylist.uid = uid
            mylist.listKind = 'todo'
            db.session.add(mylist)
            db.session.commit()
                        
            response_object = {
                'status': 'success',
                'message': '유저선택정보를 변경했습니다'
            }
            return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '유저선택정보를 변경중 에러가 발생하였습니다'
        }
        return response_object, 401