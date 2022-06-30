from app.main.service.auth_helper import Auth
from app.main.model.list import List

def get_post(uid,postId):
    '''게시물 정보 취득'''
    post = List.query.filter_by(postId=postId).first() # 게시물 정보 취득
    user = Auth.get_user_info(post.writerUid) # 파이어베이스에 저장된 유저정보 취득
    userAuth = True if uid == post.writerUid else False #게시물 작성자 유무
    setattr(post,'writerUserName',user['nickname']) # 게시물 작성자의 닉네임등록
    setattr(post,'userAuth',userAuth) # 게시물 작성자 유무
    return post