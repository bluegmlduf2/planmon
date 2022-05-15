from app.main.model.user import User
from app.main.model.mylist import Mylist


def get_a_selection(uid):
    user=User.query.filter_by(uid=uid).first()
    mylist=Mylist.query.filter_by(uid=uid).all()
    completelist=[ x.myListId for x in mylist if x.listKind == 'todo'] # 내 리스트정보에서 할일 리스트 취득
    todolist=[ x.myListId for x in mylist if x.listKind == 'complete'] # 내 리스트정보에서 완료 리스트 취득
    setattr(user,'todolist',todolist) # 유저 객체에 할일 리스트 등록
    setattr(user,'completelist',completelist) # 유저 객체에 완료 리스트 등록
    return user