from app.main.model.list import List
from app.main.model.mylist import Mylist
from app.main.util import sort_by_id,get_next_page,get_per_page

def get_my_completelist(uid, postInfo = None):
    '''유저의 완료 리스트 취득'''
    # 페이지네이션 취득
    page = get_next_page(postInfo) # 표시할 페이지수를 취득
    per_page = get_per_page(postInfo) # 한 페이지에 표시할 게시물의 수를 취득

    postIds = None # 취득할 키값
    # 로그인 상태인경우
    if uid:
        # 서버에 저장된 내 완료 일정 취득
        postIds = [x.myListId for x in Mylist.query.filter_by(uid=uid, listKind='complete').order_by(Mylist.addedDate.desc()).all()]
    else:
    # 미로그인 상태인 경우
        # 로컬스토리지에 저장된 내 완료일정의 키값 취득
        postIds = postInfo.get('myCompletelist',None)

    my_completelist_query = List.query.filter(List.postId.in_(postIds)).order_by(sort_by_id(postIds))
    my_completelist_count = my_completelist_query.count() # 내 완료일정의 총 수
    my_completelist_result = my_completelist_query.paginate(page,per_page,error_out=False) # 완료일정의 페이지네이션 된 값
    
    my_completelist = {
        'my_completelist':my_completelist_result.items, # 완료일정 (받아온 키의 정렬순서대로)
        'has_next':my_completelist_result.has_next, # 다음페이지 유무
        'current_page':my_completelist_result.page, # 현재페이지
        'total_count':my_completelist_count, # 총 완료일정 건수
    }

    return my_completelist