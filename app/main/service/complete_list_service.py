from app.main import db
from app.main.model.list import List
from app.main.model.mylist import Mylist
from app.main.model.user import User
from sqlalchemy import exc
from app.main.util import sort_by_id
from app.main.service import get_next_page,get_per_page,get_filter_condition_by_searchword

def get_my_completelist(uid, postInfo = None):
    '''유저의 완료 리스트 취득'''
    # 페이지네이션 취득
    page = get_next_page(postInfo) # 표시할 페이지수를 취득
    per_page = get_per_page(postInfo) # 한 페이지에 표시할 게시물의 수를 취득

    # 로그인 상태인경우
    if uid:
        # 서버에 저장된 내 완료 일정 취득
        postIds = [x.myListIdRef for x in Mylist.query.filter_by(uid=uid, listKind='complete').order_by(Mylist.addedDate.desc()).all()]
    else:
    # 미로그인 상태인 경우
        # 로컬스토리지에 저장된 내 완료일정의 키값 취득
        postIds = postInfo.get('myCompletelist',None)

    # 재검색시 사용하는 검색조건
    filter_searchWord = get_filter_condition_by_searchword(postInfo)

    # 내 완료일정의 상세 정보 취득
    my_completelist_query = List.query.filter(List.postId.in_(postIds)).\
        filter(filter_searchWord).\
        order_by(sort_by_id(postIds))

    # 완료일정의 페이지네이션 된 값
    my_completelist_result = my_completelist_query.paginate(page,per_page,error_out=False)
    
    my_completelist = {
        'my_completelist':my_completelist_result.items, # 완료일정 (받아온 키의 정렬순서대로)
        'has_next':my_completelist_result.has_next, # 다음페이지 유무
        'current_page':my_completelist_result.page, # 현재페이지
        'total_count':len(postIds), # 총 완료일정 수
    }

    return my_completelist

def destroy_completelist(uid,postId):
    '''유저의 완료일정을 삭제함'''
    try:
        user=User.query.filter_by(uid=uid).first()
        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            # 기존 데이터 삭제
            Mylist.query.filter_by(uid=uid, myListIdRef=postId).delete()
            # 커밋
            db.session.commit()
                        
            response_object = {
                'status': 'success',
                'message': '완료일정을 삭제했습니다'
            }
            return response_object, 201
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 삭제된 일정입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '완료일정 삭제중 에러가 발생하였습니다'
        }
        return response_object, 401