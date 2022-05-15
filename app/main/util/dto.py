from flask_restx import Namespace, fields

class SelectionDto:
    api = Namespace('selection', description='유저선택정보')
    list = api.model('list', {
        'postId': fields.String(description='일정 ID'),
        'title': fields.String(description='일정 제목'),
    }) # 리스트의 스키마
    selection = api.model('selection', {
        'completelist': fields.List(description='완료일정리스트', default=[], cls_or_instance=fields.String()),
        'country': fields.String(description='선택국가'),
        'entryDate': fields.Date(description='입국날짜'),
        'isShowMessage': fields.Boolean(required=True, default=False, description='경고메세지표시유무'),
        'stayStatus': fields.String( description='체류상태'),
        'todolist': fields.List(description='할일일정리스트', default=[], cls_or_instance=fields.Nested(list)),    
    })


class ListDto:
    api = Namespace('list', description='일정관리')
    list = api.model('list', {
        'postId': fields.String(description='일정 ID'),
        'title': fields.String(description='일정 제목'),
    })


class UserDto:
    api = Namespace('user', description='유저정보')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
