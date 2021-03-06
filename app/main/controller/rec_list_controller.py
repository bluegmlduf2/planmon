from flask_restx import Resource

from app.main.util.decorator import token_required, get_user_by_token
from ..util.dto import RecListDto
from ..service.rec_list_service import get_reclist, update_reclist
import json

api = RecListDto.api
_reclist = RecListDto.reclist


@api.route('/<param>')
@api.param('param', '유저의 선택정보 혹은 추가한 추천일정')
class RecList(Resource):
    @get_user_by_token
    @api.doc('추천 일정 가져오기')
    @api.marshal_list_with(_reclist, envelope='data')
    def get(uid,self,param):
        """할일 일정을 반환"""
        selection = json.loads(param) #유저의 선택정보
        return get_reclist(uid,selection)

    @token_required
    @api.doc('로그인한 유저의 추천일정을 추가')
    def put(uid,self,param):
        """유저의 추천일정을 추가함"""
        postId = param # 유저가 추가한 추천일정
        return update_reclist(uid,postId)