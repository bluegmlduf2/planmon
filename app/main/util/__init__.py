def sort_by_id(ids,list):
    '''매개변수로 전달된 리스트의 순서를 postIds의 순서에 맞춰 변경한다'''
    sorted_list= [] # 정렬된 배열순서
    for x in ids:
        for y in list:
            if x == y.postId:
                sorted_list.append(y)
    return sorted_list

def remove_unnecessary_elements(selection):
    '''SQL의 조건 매개변수에 불필요한 칼럼을 제거한다'''
    necessary_elements = ['country','stayStatus'] # 필요한 칼럼
    # 값이 존재하고, 필요한 칼럼만 남겨서 검색을 위한 딕셔너리로 반환
    filters={k: v for k, v in selection.items() if v is not None and k in necessary_elements}
    return filters

def get_next_page(selection):
    # 다음페이지를 가져온다 만약 가져올 페이지가 존재하지 않으면 1페이지를 가져온다
    return selection['currentPage']+1 if selection.get('currentPage',False) else 1 

def get_per_page(selection):
    # 한 페이지에 표시할 게시물의 수를 취득, 존재하지 않을 경우 10개씩 표시한다
    return  20 if selection.get('get20perpage',False) else 10