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

def remove_unnecessary_elements(selection):
    '''SQL의 조건 매개변수에 불필요한 칼럼을 제거한다'''
    necessary_elements = ['country','stayStatus'] # 필요한 칼럼
    # 값이 존재하고, 필요한 칼럼만 남겨서 검색을 위한 딕셔너리로 반환
    filters={k: v for k, v in selection.items() if v is not None and k in necessary_elements}
    return filters

def get_next_page(selection):
    # 페이지네이션 없이 일정만 가져오는 경우 모든 일정을 표시한다
    if selection is None:
        return 1
    # 모든일정의 초기화시 모든 일정을 표시한다
    elif selection.get('getAllPages',False):
        return 1
    else:
        # 다음페이지를 가져온다 만약 가져올 페이지가 존재하지 않으면 1페이지를 가져온다
        return selection['currentPage']+1 if selection.get('currentPage',False) else 1 

def get_per_page(selection):
    # 페이지네이션 없이 일정만 가져오는 경우 모든 일정을 표시한다
    if selection is None:
        return 10000
    # 모든일정의 초기화시 모든 일정을 표시한다
    elif selection.get('getAllPages',False):
        return 10000
    else:
    # 한 페이지에 표시할 게시물의 수를 취득, 존재하지 않을 경우 10개씩 표시한다
        return  20 if selection.get('get20perpage',False) else 10