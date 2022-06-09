from flask_restx import Resource

from app.main.util.decorator import get_user_by_token
from ..util.dto import CompleteListDto
from ..service.complete_list_service import get_my_completelist
import json

api = CompleteListDto.api
_completelist = CompleteListDto.completelist
@api.route('/<postInfo>')
@api.param('postInfo', '완료 일정 리스트')
class CompleteList(Resource):
    @api.doc('완료 일정 가져오기')
    @get_user_by_token
    @api.marshal_list_with(_completelist, envelope='data')
    def get(uid,self,postInfo):
        """완료 일정을 반환"""
        return get_my_completelist(uid,json.loads(postInfo))