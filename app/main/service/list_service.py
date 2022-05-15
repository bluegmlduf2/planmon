from app.main.model.list import List
from app.main.model.mylist import Mylist
from sqlalchemy.orm import load_only

def get_todolist(uid):
    '''유저의 할일 리스트 취득'''
    my_todolist_id = Mylist.query.filter_by(uid=uid, listKind='todo').all() # 내가 등록한 할일일정의 키값 취득
    my_todolist_id_list = [x.myListId for x in my_todolist_id]
    my_list = List.query.filter(List.postId.in_(my_todolist_id_list)).all() # 일정 테이블에서 내 할일 일정 취득
    return my_list