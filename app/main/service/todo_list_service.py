from app.main.model.list import List
from app.main.model.mylist import Mylist
from  app.main.util import sort_by_id

def get_my_todolist(uid):
    '''유저의 할일 리스트 취득'''
    my_todolist_id_list = [x.myListId for x in Mylist.query.filter_by(uid=uid, listKind='todo').order_by(Mylist.addedDate.desc()).all()] # 내가 등록한 할일일정의 키값 취득
    my_todolist = List.query.filter(List.postId.in_(my_todolist_id_list)).all() # 일정 테이블에서 내 할일 일정 취득
    return my_todolist

def get_todolist_by_id(postIds):
    '''일정의 키로 할일 리스트 취득'''
    todolist = List.query.filter(List.postId.in_(postIds)).all() # 일정 테이블에서 내 할일 일정 취득
    # 매개변수로 전달된 postIds의 순서대로 변경한다
    return sort_by_id(postIds,todolist)
