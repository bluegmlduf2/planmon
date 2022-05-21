from app.main.model.user import User
from app.main.model.mylist import Mylist
from app.main.service.todo_list_service import get_my_todolist

def get_a_selection(uid):
    '''유저선택정보를 취득'''
    user=User.query.filter_by(uid=uid).first()
    mylist=Mylist.query.filter_by(uid=uid).all()
    todolist=get_my_todolist(uid)  # 내 리스트정보에서 할일 리스트 취득
    completelist=[ x.myListId for x in mylist if x.listKind == 'complete'] # 내 리스트정보에서 완료 리스트 취득
    setattr(user,'myTodolist',todolist) # 유저 객체에 할일 리스트 등록
    setattr(user,'myCompletelist',completelist) # 유저 객체에 완료 리스트 등록
    return user