from app.main.model.list import List
from app.main.model.mylist import Mylist
from app.main.util import sort_by_id,get_next_page,get_per_page

def get_my_completelist(uid):
    '''유저의 완료 리스트 취득'''
    my_completelist_id_list = [x.myListId for x in Mylist.query.filter_by(uid=uid, listKind='complete').order_by(Mylist.addedDate.desc()).all()] # 내가 등록한 할일일정의 키값 취득
    my_completelist = List.query.filter(List.postId.in_(my_completelist_id_list)).all() # 일정 테이블에서 내 할일 일정 취득
    return my_completelist

def get_completelist_by_id(postInfo):
    '''일정의 키로 완료 리스트 취득'''
    # 페이지네이션 취득
    page = get_next_page(postInfo) # 표시할 페이지수를 취득
    per_page = get_per_page(postInfo) # 한 페이지에 표시할 게시물의 수를 취득

    # 화면에서 취득한 할일일정의 키값
    postIds = postInfo.get('myCompletelist',None)

    my_completelist_query = List.query.filter(List.postId.in_(postIds)).order_by(sort_by_id(postIds)).paginate(page,per_page,error_out=False) # 일정 테이블에서 내 할일 일정 취득
    # 매개변수로 전달된 postIds의 순서대로 변경한다

    my_completelist = {
        'my_completelist':my_completelist_query.items, # 완료일정 (받아온 키의 정렬순서대로)
        'has_next':my_completelist_query.has_next, # 다음페이지 유무
        'current_page':my_completelist_query.page, # 현재페이지
        'total_count':len(postInfo['myCompletelist']), # 총 완료일정 건수
    }

    return my_completelist