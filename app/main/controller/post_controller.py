from flask_restx import Resource

from app.main.util.decorator import get_user_by_token
from ..util.dto import PostDto
from ..service.post_service import get_post,get_post_detail
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


@api.route('/<param>/<requestItem>')
@api.param('param', '게시물 번호')
@api.param('requestItem', '게시물에서 취득할 정보')
class PostDetail(Resource):
    @api.marshal_with(_post, envelope='data')
    def get(self,param,requestItem):
        """게시물에서 특정 정보만 취득"""
        return get_post_detail(param,requestItem)