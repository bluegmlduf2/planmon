from flask_restx import Resource

from app.main.util.decorator import get_user_by_token
from ..util.dto import TodoListDto
from ..service.todo_list_service import get_todolist_by_id, get_my_todolist
import json

api = TodoListDto.api
_todolist = TodoListDto.todolist
@api.route('/<postIds>')
@api.param('postIds', '할일 일정 리스트')
class TodoList(Resource):
    @api.doc('할일 일정 가져오기')
    @get_user_by_token
    @api.marshal_list_with(_todolist, envelope='data')
    def get(uid,self,postIds):
        # 로그인 유무에 따라 전달값이 다르다
        if uid:
            """나의 할일 일정을 반환"""
            return get_my_todolist(uid)
        else:
            """로컬 스토리지의 할일 일정을 반환"""
            return get_todolist_by_id(json.loads(postIds))