from flask_restx import Namespace, fields


class SelectionDto:
    api = Namespace('selection', description='유저선택정보')
    listSchema = api.model('listSchema', {
        'postId': fields.String(description='일정 ID'),
        'title': fields.String(description='일정 제목'),
        'stayStatus': fields.String(description='일정 체류상태'),
    })# 리스트의 스키마
    selection = api.model('selection', {
        'myCompletelist': fields.List(description='완료일정리스트', default=[], cls_or_instance=fields.Nested(listSchema)),
        'country': fields.String(description='선택국가'),
        'entryDate': fields.Date(description='입국날짜'),
        'isShowMessage': fields.Boolean(required=True, default=False, description='경고메세지표시유무'),
        'stayStatus': fields.String( description='체류상태'),
        'myTodolist': fields.List(description='할일일정리스트', default=[], cls_or_instance=fields.Nested(listSchema)),
        'todolistCount': fields.Integer(description='총 할일일정수'),
        'completelistCount': fields.Integer(description='총 완료일정수'),    
    })

class TodoListDto:
    api = Namespace('todolist', description='할일일정관리')
    listSchema = api.model('listSchema', {
        'postId': fields.String(description='일정 ID'),
        'title': fields.String(description='일정 제목'),
        'stayStatus': fields.String(description='일정 체류상태'),
    })# 리스트의 스키마
    todolist = api.model('todolist', {
        'my_todolist': fields.List(description='할일일정리스트', default=[], cls_or_instance=fields.Nested(listSchema)),
        'has_next': fields.Boolean(description='다음페이지 유무'),
        'current_page': fields.Integer(description='현재 페이지'),
        'total_count': fields.Integer(description='총 할일일정 수'),
    })

class CompleteListDto:
    api = Namespace('completelist', description='완료일정관리')
    listSchema = api.model('listSchema', {
        'postId': fields.String(description='일정 ID'),
        'title': fields.String(description='일정 제목'),
        'stayStatus': fields.String(description='일정 체류상태'),
    })# 리스트의 스키마
    completelist = api.model('completelist', {
        'my_completelist': fields.List(description='완료일정리스트', default=[], cls_or_instance=fields.Nested(listSchema)),
        'has_next': fields.Boolean(description='다음페이지 유무'),
        'current_page': fields.Integer(description='현재 페이지'),
        'total_count': fields.Integer(description='총 완료일정 수'),
    })

class RecListDto:
    api = Namespace('reclist', description='추천일정관리')
    listSchema = api.model('listSchema', {
        'postId': fields.String(description='일정 ID'),
        'title': fields.String(description='일정 제목'),
        'stayStatus': fields.String(description='일정 체류상태'),
    })# 리스트의 스키마
    reclist = api.model('reclist', {
        'my_reclist': fields.List(description='추천일정리스트', default=[], cls_or_instance=fields.Nested(listSchema)),
        'has_next': fields.Boolean(description='다음페이지 유무'),
        'current_page': fields.Integer(description='현재 페이지'),
        'total_count': fields.Integer(description='총 추천일정 수'),
    })

class PostDto:
    api = Namespace('post', description='게시물정보')
    post = api.model('post', {
        'postId': fields.String(description='게시물 번호'),
        'writerUserName': fields.String(description='게시물 작성자'),
        'title': fields.String(description='게시물 제목'),
        'content': fields.String(description='게시물 내용'),
        'stayStatus': fields.String(description='체류상태'),
        'isAdded': fields.Boolean(description='추가된 일정 유무'),
        'postViewCount': fields.Integer(description='조회수'),
        'afterEntryDate': fields.Integer(description='입국경과일'),
        'startDate': fields.Date(description='일정시작일'),
        'endDate': fields.Date(description='일정종료일'),
        'createdDate': fields.Date(description='게시글작성일'),
        'userAuth': fields.Boolean(description='게시글작성자유무'),
        'myStartDate': fields.Date(description='나의 일정 시작일'),
        'myEndDate': fields.Date(description='나의 일정 종료일'),
    })

class MyListDto:
    api = Namespace('mylist', description='내가 작성한 일정관리')
    listSchema = api.model('listSchema', {
        'postId': fields.String(description='일정 ID'),
        'title': fields.String(description='일정 제목'),
        'stayStatus': fields.String(description='일정 체류상태'),
    })# 리스트의 스키마
    mylist = api.model('mylist', {
        'my_list': fields.List(description='내가 작성한 일정리스트', default=[], cls_or_instance=fields.Nested(listSchema)),
        'has_next': fields.Boolean(description='다음페이지 유무'),
        'current_page': fields.Integer(description='현재 페이지'),
        'total_count': fields.Integer(description='총 추천일정 수'),
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
