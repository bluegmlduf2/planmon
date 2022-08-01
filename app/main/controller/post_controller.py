from flask_restx import Resource
from flask import request

from app.main.util.decorator import token_required,get_user_by_token,exception_handler
from ..util.dto import PostDto
from ..util.dto import PostUpdateDateDto
from ..service.post_service import get_post,get_post_detail,update_post_date,create_post,update_post

api = PostDto.api
_post = PostDto.post
_postupdatedate = PostUpdateDateDto.postupdatedate


@api.route('/<param>')
@api.param('param', '게시물 번호')
class Post(Resource):
    @get_user_by_token
    @exception_handler
    @api.doc('게시물 가져오기')
    @api.marshal_list_with(_post, envelope='data')
    def get(uid,self,param):
        """게시물 정보를 반환"""
        return get_post(uid,param)

@api.route('')
class PostWrite(Resource):
    @token_required
    @exception_handler
    @api.doc('게시물 등록')
    @api.marshal_list_with(_post, envelope='data')
    def post(uid,self):
        """게시물 정보를 등록"""
        payload = request.json
        return create_post(uid,payload)

    @token_required
    @exception_handler
    @api.doc('게시물 수정')
    @api.marshal_list_with(_post, envelope='data')
    def put(uid,self):
        """게시물 정보를 수정"""
        payload = request.json
        return update_post(uid,payload)


@api.route('/<param>/<requestItem>')
@api.param('param', '게시물 번호')
@api.param('requestItem', '게시물에서 취득할 정보')
class PostDetail(Resource):
    @exception_handler
    @api.doc('게시물의 선택정보 가져오기')
    @api.marshal_with(_post, envelope='data')
    def get(self,param,requestItem):
        """게시물에서 특정 정보만 취득"""
        return get_post_detail(param,requestItem)


@api.route('/update-post-date')
class PostUpdateDate(Resource):
    @token_required
    @exception_handler
    @api.doc('게시물의 일정시적일과 일정종료일을 갱신')
    @api.marshal_with(_postupdatedate, envelope='data')
    def put(uid,self):
        """게시물의 일정시작일과 종료일을 갱신"""
        payload = request.json
        return update_post_date(uid,payload)