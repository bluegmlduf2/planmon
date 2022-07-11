from flask_restx import Resource
from flask import request

from app.main.util.decorator import get_user_by_token,token_required
from ..util.dto import CommentDto
from ..service.comment_service import get_comment,create_comment
import json

api = CommentDto.api
_comment = CommentDto.comment

@api.route('/<param>')
@api.param('param', '게시물 번호')
class Comment(Resource):
    @get_user_by_token
    @api.doc('댓글 가져오기')
    @api.marshal_list_with(_comment, envelope='data')
    def get(uid,self,param):
        """댓글 정보를 반환"""
        return get_comment(uid,param)

    @token_required
    @api.doc('댓글 등록하기')
    def post(uid,self,param):
        """댓글 정보를 등록"""
        payload = request.json
        return create_comment(uid,payload)