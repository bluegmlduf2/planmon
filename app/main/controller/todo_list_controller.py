from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import TodoListDto
from ..service.todo_list_service import get_todolist_by_id, get_my_todolist
import json

api = TodoListDto.api
_todolist = TodoListDto.todolist


@api.route('/<postIds>')
@api.param('postIds', '검색할 할일 일정 키 리스트')
class TodoList(Resource):
    @api.doc('검색한 할일 일정 가져오기')
    @api.marshal_list_with(_todolist, envelope='data')
    def get(self,postIds):
        """할일 일정을 반환"""
        return get_todolist_by_id(json.loads(postIds))


@api.route('/mytodolist')
class MyTodoList(Resource):
    @api.doc('나의 할일 일정 가져오기')
    @token_required
    @api.marshal_list_with(_todolist, envelope='data')
    def get(uid,self):
        """나의 할일 일정을 반환"""
        return get_my_todolist(uid)