from app.main.model.list import List
from sqlalchemy import case

def sort_by_id(postIds):
    '''매개변수로 전달된 리스트의 순서를 postIds의 순서에 맞춰 변경한다'''
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
    if selection.get('getAllPages',False):
    # 모든일정은 모든 페이지를 표시한다
        return 1
    else:
        # 다음페이지를 가져온다 만약 가져올 페이지가 존재하지 않으면 1페이지를 가져온다
        return selection['currentPage']+1 if selection.get('currentPage',False) else 1 

def get_per_page(selection):
    if selection.get('getAllPages',False):
    # 모든일정은 모든 페이지를 표시한다
        return 10000
    else:
    # 한 페이지에 표시할 게시물의 수를 취득, 존재하지 않을 경우 10개씩 표시한다
        return  20 if selection.get('get20perpage',False) else 10