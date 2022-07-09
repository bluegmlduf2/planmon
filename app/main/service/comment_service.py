from app.main import db

from app.main.model.comment import Comment
from app.main.service.auth_helper import Auth
from app.main.model.commentreply import CommentReply

def get_comment(uid,postId):
    '''댓글 정보 취득'''
    # 댓글과 대댓글 정보취득
    comment = db.session.query(Comment,CommentReply).\
        outerjoin(CommentReply,Comment.commentId == CommentReply.commentReplyRefId).\
        filter(Comment.postIdRef==postId).all()
    
    commentResult = []

    # 댓글과 대댓글의 정보를 변환
    for c in comment:
        # 데이터를 클래스 -> 딕셔너리로 변경
        commentData=vars(c[0]) # 댓글데이터
        commentReplyData=vars(c[1]) if c[1] else None # 대댓글데이터

        # 댓글데이터
        comment_user = Auth.get_user_info(commentData['commentUid']) # 파이어베이스에 저장된 유저정보 취득
        comment_user_auth = True if uid == commentData['commentUid'] else False #댓글 작성자 유무
        commentData['commentUserName'] = comment_user['nickname'] # 댓글 작성자의 닉네임등록
        commentData['commentUserAuth'] = comment_user_auth # 댓글 작성자 유무

        # 대댓글데이터
        if commentReplyData:
            comment_reply_user = Auth.get_user_info(commentReplyData['commentReplyUid']) # 파이어베이스에 저장된 유저정보 취득
            comment_user_reply_auth = True if uid == commentReplyData['commentReplyUid'] else False #대댓글 작성자 유무
            commentReplyData['commentReplyUserName'] = comment_reply_user['nickname'] # 대댓글 작성자의 닉네임등록
            commentReplyData['commentReplyUserAuth'] = comment_user_reply_auth # 대댓글 작성자 유무
            commentData['commentReply'] = commentReplyData # 댓글에 대댓글정보 등록
        
        # 변환이 끝난 댓글,대댓글 데이터를 반환값에 설정
        commentResult.append(commentData)
        
    return commentResult

