from flask_restx import Resource
from flask import request

from app.main.util.decorator import token_required
from ..util.dto import CommentReplyDto
from ..service.comment_reply_service import create_comment_reply

api = CommentReplyDto.api

@api.route('')
class CommentReply(Resource):
    @token_required
    @api.doc('대댓글 등록하기')
    def post(uid,self):
        """대댓글 정보를 등록"""
        payload = request.json
        return create_comment_reply(uid,payload)