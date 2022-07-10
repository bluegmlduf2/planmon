from app.main import db

from app.main.model.comment import Comment
from app.main.service.auth_helper import Auth
from app.main.model.commentreply import CommentReply

def get_comment(uid,postId):
    '''댓글 정보 취득'''
    # 댓글과 대댓글 정보취득
    comment = db.session.query(Comment).\
        outerjoin(CommentReply,Comment.commentId == CommentReply.commentReplyRefId).\
        filter(Comment.postIdRef==postId).\
        order_by(Comment.commentAddedDate).all()

        # 댓글과 대댓글의 정보를 변환
    for c in comment:
        commentData=c # 댓글데이터
        commentReplyData=c.commentReply # 대댓글데이터

        # 댓글데이터
        comment_user = Auth.get_user_info(commentData.commentUid) # 파이어베이스에 저장된 유저정보 취득
        comment_user_auth = True if uid == commentData.commentUid else False #댓글 작성자 유무
        setattr(commentData,'commentUserName',comment_user['nickname']) # 댓글 작성자의 닉네임등록
        setattr(commentData,'commentUserAuth',comment_user_auth) # 댓글 작성자 유무

        # 대댓글데이터
        if commentReplyData:
            for commentReply in commentReplyData:
                comment_reply_user = Auth.get_user_info(commentReply.commentReplyUid) # 파이어베이스에 저장된 유저정보 취득
                comment_user_reply_auth = True if uid == commentReply.commentReplyUid else False #대댓글 작성자 유무
                setattr(commentReply,'commentReplyUserName',comment_reply_user['nickname']) # 대댓글 작성자의 닉네임등록
                setattr(commentReply,'commentReplyUserAuth',comment_user_reply_auth) # 대댓글 작성자 유무

    return comment

