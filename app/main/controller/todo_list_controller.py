from flask_restx import Resource

from app.main.util.decorator import token_required,get_user_by_token
from ..util.dto import TodoListDto
from ..service.todo_list_service import get_my_todolist,update_todolist,destroy_todolist
import json

api = TodoListDto.api
_todolist = TodoListDto.todolist
@api.route('/<param>')
@api.param('param', '할일 일정 리스트')
class TodoList(Resource):
    @get_user_by_token
    @api.doc('할일 일정 가져오기')
    @api.marshal_list_with(_todolist, envelope='data')
    def get(uid,self,param):
        """할일 일정을 반환"""
        return get_my_todolist(uid,json.loads(param))

    @token_required
    @api.doc('로그인한 유저의 할일일정을 추가')
    def put(uid,self,param):
        """유저의 할일일정을 추가함"""
        postId = param # 유저가 추가한 추천일정
        return update_todolist(uid,postId)

    @token_required
    @api.doc('로그인한 유저의 할일일정을 삭제')
    def delete(uid,self,param):
        """유저의 할일일정을 삭제함"""
        postId = param # 유저가 삭제한 추천일정
        return destroy_todolist(uid,postId)