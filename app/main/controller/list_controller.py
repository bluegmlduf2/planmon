from flask_restx import Resource

from app.main.util.decorator import get_user_by_token
from ..util.dto import ListDto
from ..service.list_service import get_todolist
from typing import Dict, Tuple

api = ListDto.api
_list = ListDto.list


@api.route('/todolist')
class TodoList(Resource):
    @api.doc('할일 일정 가져오기')
    @get_user_by_token
    @api.marshal_list_with(_list, envelope='data')
    def get(uid,self):
        """할일 일정을 반환"""
        return get_todolist(uid)