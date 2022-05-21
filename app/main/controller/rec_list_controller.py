from flask_restx import Resource

from ..util.dto import RecListDto
from ..service.rec_list_service import get_reclist
import json

api = RecListDto.api
_reclist = RecListDto.reclist


@api.route('/')
@api.route('/<selection>')
@api.param('selection', '유저의 선택정보')
class RecList(Resource):
    @api.doc('추천 일정 가져오기')
    @api.marshal_list_with(_reclist, envelope='data')
    def get(self,selection):
        """할일 일정을 반환"""
        return get_reclist(json.loads(selection))