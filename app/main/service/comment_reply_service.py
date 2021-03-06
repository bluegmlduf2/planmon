from app.main import db

from app.main.model.commentreply import CommentReply
from app.main.model.user import User
from sqlalchemy import exc


def create_comment_reply(uid,param):
    '''대댓글 등록'''
    try:
        user=User.query.filter_by(uid=uid).first()
        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            comment_reply = CommentReply()
            comment_reply.commentReplyContent = param['commentReplyContent']
            comment_reply.commentReplyRefId = param['commentId']
            comment_reply.commentReplyUid = uid

            db.session.add(comment_reply)
            db.session.commit()
                        
            response_object = {
                'status': 'success',
                'message': '대댓글을 등록했습니다'
            }
            return response_object, 201
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 등록된 대댓글입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '대댓글 등록중 에러가 발생하였습니다'
        }
        return response_object, 401

def update_comment_reply(uid,param):
    '''대댓글 수정'''
    try:
        user=User.query.filter_by(uid=uid).first()
        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            comment_reply = CommentReply.query.filter_by(commentReplyUid=uid, commentReplyId=param['commentReplyId']).first()
            comment_reply.commentReplyContent = param['commentReplyContent']

            db.session.add(comment_reply)
            db.session.commit()
                        
            response_object = {
                'status': 'success',
                'message': '대댓글을 수정했습니다'
            }
            return response_object, 201        
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 수정된 대댓글입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '대댓글 수정중 에러가 발생하였습니다'
        }
        return response_object, 401

def destroy_comment_reply(uid,commentReplyId):
    '''대댓글 삭제'''
    try:
        user=User.query.filter_by(uid=uid).first()
        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            CommentReply.query.filter_by(commentReplyUid=uid, commentReplyId=commentReplyId).delete()

            db.session.commit()
                        
            response_object = {
                'status': 'success',
                'message': '대댓글을 삭제했습니다'
            }
            return response_object, 201
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 삭제된 대댓글입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '대댓글 삭제중 에러가 발생하였습니다'
        }
        return response_object, 401