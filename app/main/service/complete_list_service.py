from app.main.model.list import List
from app.main.model.mylist import Mylist

def get_my_completelist(uid):
    '''유저의 완료 리스트 취득'''
    my_completelist_id_list = [x.myListId for x in Mylist.query.filter_by(uid=uid, listKind='complete').order_by(Mylist.addedDate.desc()).all()] # 내가 등록한 할일일정의 키값 취득
    my_completelist = List.query.filter(List.postId.in_(my_completelist_id_list)).all() # 일정 테이블에서 내 할일 일정 취득
    return my_completelist

def get_completelist_by_id(postIds):
    '''일정의 키로 완료 리스트 취득'''
    completelist = List.query.filter(List.postId.in_(postIds)).all() # 일정 테이블에서 내 할일 일정 취득
    completelist_sorted= [] # 정렬된 배열순서
    # 매개변수로 전달된 postIds의 순서대로 변경한다
    for x in postIds:
        for y in completelist:
            if x == y.postId:
                completelist_sorted.append(y)
    return completelist_sorted