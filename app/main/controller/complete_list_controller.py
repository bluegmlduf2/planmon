from flask_restx import Resource

from app.main.util.decorator import get_user_by_token
from ..util.dto import CompleteListDto
from ..service.complete_list_service import get_completelist_by_id, get_my_completelist
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
        # 로그인 유무에 따라 전달값이 다르다
        if uid:
            """나의 완료 일정을 반환"""
            return get_my_completelist(uid)
        else:
            """로컬 스토리지의 완료 일정을 반환"""
            return get_completelist_by_id(json.loads(postInfo))