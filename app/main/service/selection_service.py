from app.main.model.user import User
from app.main.service.todo_list_service import get_my_todolist
from app.main.service.complete_list_service import get_my_completelist

def get_a_selection(uid):
    '''유저선택정보를 취득'''
    user=User.query.filter_by(uid=uid).first()
    todolist=get_my_todolist(uid)  # 내 할일일정 정보 취득
    completelist=get_my_completelist(uid)  # 내 완료일정 정보 취득
    setattr(user,'myTodolist',todolist['my_todolist']) # 내 할일일정 정보에서 일정 취득후 등록
    setattr(user,'myCompletelist',completelist['my_completelist']) # 내 완료일정 정보에서 일정 취득후 등록
    setattr(user,'todolistCount',todolist['total_count']) # 나의 총 할일 일정 취득후 등록
    setattr(user,'completelistCount',completelist['total_count']) # 나의 총 완료 일정 취득후 등록
    return user