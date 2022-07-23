from app.main import db
from app.main.service.auth_helper import Auth
from app.main.model.list import List
from app.main.model.mylist import Mylist
from app.main.model.user import User
from app.main.util import convert_string_to_date,get_current_time,moveImageFile
from app.main.service.comment_service import get_comment
from app.main.service.rec_list_service import update_reclist
from sqlalchemy import exc
from datetime import datetime


def get_post(uid,postId):
    '''게시물 정보 취득'''
    # 게시물 관련
    post = List.query.filter_by(postId=postId).first() # 게시물 정보 취득

    # 유저정보 관련
    user = Auth.get_user_info(post.writerUid) # 파이어베이스에 저장된 유저정보 취득
    userAuth = True # 게시물 작성자인 경우
    isAdded = bool(Mylist.query.filter_by(myListIdRef=postId,uid=uid).count()) # 이미 추가한 일정유무
    isCompleted = bool(Mylist.query.filter_by(myListIdRef=postId,uid=uid,listKind='complete').count()) # 완료 일정유무
    
    # 게시물 작성자가 아닌 경우
    if uid != post.writerUid:
        userAuth = False # 게시물 작성자가 아닌 경우
        update_view_count(post) # 게시물의 조회수 증가

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
    
    # 댓글과 대댓글정보 등록
    comment = get_comment(uid,postId)
    setattr(post,'comment', comment)

    return post


def create_post(uid,payload):
    '''게시글 등록'''
    try:
        user=User.query.filter_by(uid=uid).first()
        
        # 유저의 선택정보가 전부 입력되어있는지 확인
        if not user.entryDate or not user.country or not user.stayStatus:
            raise Exception('TODO에러처리')

        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            # 화면에서 입력한 데이터
            inputData = payload['inputData']

            # 시간 데이터
            startDate = datetime.strptime(inputData['startDate'],'%Y-%m-%d') # 일정시작일
            endDate = datetime.strptime(inputData['endDate'],'%Y-%m-%d') # 일정종료일
            entryDate = datetime.strptime(user.entryDate.strftime('%Y-%m-%d'),'%Y-%m-%d') # 나의 입국날짜
            currentDate = datetime.strptime(get_current_time().strftime('%Y-%m-%d'),'%Y-%m-%d') # 현재시간
            afterEntryDate = (currentDate-entryDate).days # 내 입국후 경과 일수

            # 글내용의 이미지 url변경
            filteredContent = inputData['content'].replace(
                'api/image/temp/', 'api/image/post/')
            inputData['content'] = filteredContent

            # 게시글의 임시 이미지 파일을 저장용 폴더에 이동
            moveImageFile(inputData['tempImages'])            
            
            # 등록할 게시물 정보입력
            post = List()
            post.writerUid = uid
            post.title = inputData['title']
            post.content = inputData['content']
            post.country = inputData['country']
            post.stayStatus = inputData['stayStatus']
            post.afterEntryDate = afterEntryDate
            post.startDate = startDate
            post.endDate = endDate

            db.session.add(post)
            db.session.commit()

            
            # 다가오는 일정에 추가 
            update_reclist(uid,post.postId)

            response_object = {
                'status': 'success',
                'message': '게시글을 등록했습니다',
                'postId': post.postId
            }
            return response_object, 201
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 등록된 게시글입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '게시글 등록중 에러가 발생하였습니다'
        }
        return response_object, 401


def update_post(uid,payload):
    '''게시글 수정'''
    try:
        user=User.query.filter_by(uid=uid).first()

        # 유저의 선택정보가 전부 입력되어있는지 확인
        if not user.entryDate or not user.country or not user.stayStatus:
            raise Exception('TODO에러처리')

        # 기존 유저가 존재할 경우 유저선택정보를 갱신
        if user:
            # 화면에서 입력한 데이터
            inputData = payload['inputData']

            # 시간 데이터
            startDate = datetime.strptime(inputData['startDate'],'%Y-%m-%d') # 일정시작일
            endDate = datetime.strptime(inputData['endDate'],'%Y-%m-%d') # 일정종료일
            entryDate = datetime.strptime(user.entryDate.strftime('%Y-%m-%d'),'%Y-%m-%d') # 나의 입국날짜
            currentDate = datetime.strptime(get_current_time().strftime('%Y-%m-%d'),'%Y-%m-%d') # 현재시간
            afterEntryDate = (currentDate-entryDate).days # 내 입국후 경과 일수

            # 글내용의 이미지 url변경
            filteredContent = inputData['content'].replace(
                'api/image/temp/', 'api/image/post/')
            inputData['content'] = filteredContent

            # 게시글의 임시 이미지 파일을 저장용 폴더에 이동
            moveImageFile(inputData['tempImages'])       

            # 수정할 게시물 정보입력
            post = List.query.filter_by(writerUid=uid, postId=inputData['postId']).first()
            post.title = inputData['title']
            post.content = inputData['content']
            post.country = inputData['country']
            post.stayStatus = inputData['stayStatus']
            post.afterEntryDate = afterEntryDate
            post.startDate = startDate
            post.endDate = endDate

            db.session.add(post)
            db.session.commit()
                        
            response_object = {
                'status': 'success',
                'message': '게시글을 수정했습니다',
                'postId': post.postId
            }
            return response_object, 201
    except exc.IntegrityError as e:
        response_object = {
            'status': 'fail',
            'message': '이미 수정된 게시글입니다'
        }
        return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': '게시글 수정중 에러가 발생하였습니다'
        }
        return response_object, 401


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
