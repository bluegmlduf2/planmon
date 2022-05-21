from flask_restx import Namespace, fields


class SelectionDto:
    api = Namespace('selection', description='유저선택정보')
    listSchema = api.model('listSchema', {
        'postId': fields.String(description='일정 ID'),
        'title': fields.String(description='일정 제목'),
    })# 리스트의 스키마
    selection = api.model('selection', {
        'myCompletelist': fields.List(description='완료일정리스트', default=[], cls_or_instance=fields.String()),
        'country': fields.String(description='선택국가'),
        'entryDate': fields.Date(description='입국날짜'),
        'isShowMessage': fields.Boolean(required=True, default=False, description='경고메세지표시유무'),
        'stayStatus': fields.String( description='체류상태'),
        'myTodolist': fields.List(description='할일일정리스트', default=[], cls_or_instance=fields.Nested(listSchema)),    
    })


class TodoListDto:
    api = Namespace('todolist', description='할일일정관리')
    todolist = api.model('todolist', {
        'postId': fields.String(description='일정 ID'),
        'title': fields.String(description='일정 제목'),
    })

class RecListDto:
    api = Namespace('reclist', description='추천일정관리')
    reclist = api.model('reclist', {
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
