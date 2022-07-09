from app.main import db
from app.main.service.auth_helper import Auth
from app.main.model.list import List
from app.main.model.mylist import Mylist
from app.main.util import convert_string_to_date

def get_post(uid,postId):
    '''게시물 정보 취득'''
    # 게시물 관련
    post = List.query.filter_by(postId=postId).first() # 게시물 정보 취득
    update_view_count(post) # 게시물의 조회수 증가

    # 유저정보 관련
    user = Auth.get_user_info(post.writerUid) # 파이어베이스에 저장된 유저정보 취득
    userAuth = True if uid == post.writerUid else False #게시물 작성자 유무
    isAdded = bool(Mylist.query.filter_by(myListIdRef=postId,uid=uid).count()) # 이미 추가한 일정유무
    isCompleted = bool(Mylist.query.filter_by(myListIdRef=postId,uid=uid,listKind='complete').count()) # 완료 일정유무
    
    setattr(post,'writerUserName',user['nickname']) # 게시물 작성자의 닉네임등록
    setattr(post,'userAuth',userAuth) # 게시물 작성자 유무
    setattr(post,'isAdded',isAdded) # 추가한 일정 유무
    setattr(post,'isCompleted',isCompleted) # 완료 일정 유무

    # 로그인 유저일시 , 게시글 작성자가 아닐시 일정시작일시 등록
    if uid and not userAuth:
        mylist = Mylist.query.filter_by(myListIdRef=postId,uid=uid).first() # 게시물 정보 취득
        # 로그인 유저가 추가한 게시물인지 확인
        if mylist:
            setattr(post,'myStartDate', mylist.myStartDate ) # 로그인 유저의 일정 시작일
            setattr(post,'myEndDate', mylist.myEndDate ) # 로그인 유저의 일정 종료일               

    return post

def update_view_count(post):
    '''게시물의 조회수 증가'''
    post.postViewCount = post.postViewCount+1 
    db.session.commit()


def get_post_detail(postId,requestItem):
    """게시물에서 특정 정보만 취득"""
    post_detail_column =getattr(List,requestItem) # 취득할 데이터
    post_detail = List.query.filter_by(postId=postId).\
        with_entities(post_detail_column).first()
    return post_detail

def update_post_date(uid,param):
    '''게시물의 일정시작일과 일정종료일을 갱신'''
    try:
        # 기존 데이터 취득
        myTodoList = Mylist.query.filter_by(uid=uid, myListIdRef=param['postId']).first()

        # 일정시작일과 일정종료일을 갱신
        myTodoList.myStartDate = convert_string_to_date(param['myStartDate'])
        myTodoList.myEndDate = convert_string_to_date(param['myEndDate'])

        # 커밋
        db.session.commit()
                    
        response_object = {
            'myStartDate': myTodoList.myStartDate,
            'myEndDate': myTodoList.myEndDate
        }
        return response_object
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '일정시작일과 일정종료일을 등록중 에러가 발생하였습니다'
        }
        return response_object, 401
