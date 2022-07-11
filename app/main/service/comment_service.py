from app.main import db

from app.main.model.comment import Comment
from app.main.service.auth_helper import Auth
from app.main.model.commentreply import CommentReply
from app.main.model.user import User
from sqlalchemy import exc

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

def create_comment(uid,param):
    '''댓글 등록'''
    try:
        user=User.query.filter_by(uid=uid).first()
        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            comment = Comment()
            comment.commentContent = param['commentContent']
            comment.postIdRef = param['postId']
            comment.commentUid = uid

            db.session.add(comment)
            db.session.commit()
                        
            response_object = {
                'status': 'success',
                'message': '댓글을 등록했습니다'
            }
            return response_object, 201
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 등록된 댓글입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '댓글 등록중 에러가 발생하였습니다'
        }
        return response_object, 401

def update_comment(uid,param):
    '''댓글 수정'''
    try:
        user=User.query.filter_by(uid=uid).first()
        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            comment = Comment.query.filter_by(commentUid=uid, commentId=param['commentId']).first()
            comment.commentContent = param['commentContent']

            db.session.add(comment)
            db.session.commit()
                        
            response_object = {
                'status': 'success',
                'message': '댓글을 수정했습니다'
            }
            return response_object, 201        
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 수정된 댓글입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '댓글 수정중 에러가 발생하였습니다'
        }
        return response_object, 401

def destroy_comment(uid,commentId):
    '''댓글 삭제'''
    try:
        user=User.query.filter_by(uid=uid).first()
        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            comment_reply = CommentReply.query.filter_by(commentReplyRefId=commentId).count()
            # 대댓글이 존재하지 않는 댓글만 삭제가능
            if not comment_reply:
                Comment.query.filter_by(commentUid=uid, commentId=commentId).delete()

                db.session.commit()
                            
                response_object = {
                    'status': 'success',
                    'message': '댓글을 삭제했습니다'
                }
                return response_object, 201
            else:
                response_object = {
                    'status': 'fail',
                    'message': '대댓글이 존재하므로 삭제할수없습니다'
                }
                return response_object, 400    
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 삭제된 댓글입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '댓글 삭제중 에러가 발생하였습니다'
        }
        return response_object, 401
