from datetime import datetime
from sqlalchemy import case
from pytz import timezone
from uuid import uuid1

def get_uuid():
    '''UUID를 문자열로 취득'''
    return str(uuid1())

def get_current_time():
    '''서울기준으로 현재시간을 가져온다'''
    return datetime.now(timezone('Asia/Seoul'))

def sort_by_id(postIds):
    '''매개변수로 전달된 리스트의 순서를 postIds의 순서에 맞춰 변경한다'''
    # 순환참조 List를 import시 발생하는 순환참조에러 방지를 위해 아래와같이 import (circular import)
    from app.main.model.list import List
    
    # 사용자 정렬 (등록일순)
    if postIds:
        return case(
            {_id: index for index, _id in enumerate(postIds)},
            value=List.postId
        )
    else:
        return None