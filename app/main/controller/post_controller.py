from flask_restx import Resource

from app.main.util.decorator import get_user_by_token
from ..util.dto import PostDto
from ..service.post_service import get_post
import json

api = PostDto.api
_post = PostDto.post


@api.route('/<param>')
@api.param('param', '게시물 번호')
class Post(Resource):
    @get_user_by_token
    @api.doc('게시물 가져오기')
    @api.marshal_list_with(_post, envelope='data')
    def get(uid,self,param):
        """게시물 정보를 반환"""
        postId = json.loads(param)['postId'] # 게시물 번호
        return get_post(uid,postId)