from flask_restx import Resource
from app.main.util.dto import CompleteListDto
from app.main.service.complete_list_service import get_my_completelist,destroy_completelist
from app.main.util.decorator import get_user_by_token,token_required,exception_handler
import json

api = CompleteListDto.api
_completelist = CompleteListDto.completelist
@api.route('/<param>')
@api.param('param', '완료 일정 리스트')
class CompleteList(Resource):
    @get_user_by_token
    @exception_handler
    @api.doc('완료 일정 가져오기')
    @api.marshal_list_with(_completelist, envelope='data')
    def get(uid,self,param):
        """완료 일정을 반환"""
        return get_my_completelist(uid,json.loads(param))

    @token_required
    @exception_handler
    @api.doc('로그인한 유저의 완료일정을 삭제')
    def delete(uid,self,param):
        """유저의 완료일정을 삭제함"""
        postId = param # 유저가 삭제한 완료일정
        return destroy_completelist(uid,postId)