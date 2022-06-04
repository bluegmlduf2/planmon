from app.main.model.list import List
from app.main.model.mylist import Mylist
from app.main.util import sort_by_id,get_next_page,get_per_page

def get_my_todolist(uid):
    '''유저의 할일 리스트 취득'''
    my_todolist_id_list = [x.myListId for x in Mylist.query.filter_by(uid=uid, listKind='todo').order_by(Mylist.addedDate.desc()).all()] # 내가 등록한 할일일정의 키값 취득
    my_todolist = List.query.filter(List.postId.in_(my_todolist_id_list)).all() # 일정 테이블에서 내 할일 일정 취득
    return my_todolist

def get_todolist_by_id(postInfo):
    '''일정의 키로 할일 리스트 취득'''
    # 페이지네이션 취득
    page = get_next_page(postInfo) # 표시할 페이지수를 취득
    per_page = get_per_page(postInfo) # 한 페이지에 표시할 게시물의 수를 취득

    # 화면에서 취득한 할일일정의 키값
    postIds = postInfo.get('myTodolist',None)
    
    # 일정 테이블에서 내 할일 일정 취득
    my_todolist_qeury = List.query.filter(List.postId.in_(postIds)).order_by(sort_by_id(postIds)).paginate(page,per_page,error_out=False)

    my_todolist = {
        'my_todolist':my_todolist_qeury.items, # 할일일정 (받아온 키의 정렬순서대로)
        'has_next':my_todolist_qeury.has_next, # 다음페이지 유무
        'current_page':my_todolist_qeury.page, # 현재페이지
    }

    # 매개변수로 전달된 postIds의 순서대로 변경한다
    return my_todolist
