from app.main.model.list import List
from datetime import datetime
from pytz import timezone
from app.main.util import remove_unnecessary_elements,get_next_page,get_per_page

def get_reclist(selection):
    '''유저의 할일 리스트 취득'''
    # SQL의 검색조건 취득
    filters = remove_unnecessary_elements(selection) 
    
    # 페이지네이션 취득
    page = get_next_page(selection) # 표시할 페이지수를 취득
    per_page =get_per_page(selection) # 한 페이지에 표시할 게시물의 수를 취득

    # 추천일정에서 표시할 일정중 나의 완료일정과 할일일정을 제외함(검색조건) 
    myList = [x['postId'] for x in selection['myCompletelist']]+[x['postId'] for x in selection['myTodolist']]

    # 추천 일정 취득
    # 나의 할일일정과 완료일정제외된결과
    # 일정을 10개를 한페이지로 표시한다
    my_reclist_query = List.query.filter_by(**filters).filter(~List.postId.in_(myList)).order_by(List.createdDate.desc())
    my_reclist_result = my_reclist_query.paginate(page,per_page,error_out=False)
    my_reclist_count = my_reclist_query.count()
    my_reclist = {
        'my_reclist':my_reclist_result.items, # 추천일정
        'has_next':my_reclist_result.has_next, # 다음페이지 유무
        'current_page':my_reclist_result.page, # 현재페이지
        'total_count':my_reclist_count, # 총 추천일정 수
    }

    # 체류중인상태에서 입국후 지난 날짜의 조건이 가까운 순서로 조회
    if selection['stayStatus'] == '1' and selection['entryDate'] is not None:
        dateFormat = '%Y-%m-%d'
        entryDate = datetime.strptime(selection['entryDate'],dateFormat) # 입국날짜
        currentDate = datetime.strptime(datetime.now(timezone('Asia/Seoul')).strftime(dateFormat),dateFormat) # 현재시간
        # 만약 입국날짜가 현재시간보다 미래일 경우 일반 추천 일정반환
        if currentDate < entryDate:
            return my_reclist['my_reclist']
        diff = (currentDate-entryDate).days # 입국후 경과 일수
        # 사용자에게 유효한 추천일정을 상위에 표시한다
        # 아래의 로직은 일정의 인덱스 위치를 변경하는 로직
        added_item = []
        deleted_item = []
        for x in my_reclist['my_reclist']:
            # 사용자의 입국후 일자와 작성자의 입국후 일정시작 일자를 비교해서 유효한 리스트를 상위에 표시한다
            if diff > x.afterEntryDate:
                added_item.append(x)
                deleted_item.append(x)
        # 삭제한 아이템을 추천일정으로부터 삭제하기
        for x in deleted_item:
            my_reclist['my_reclist'].remove(x)
        # 변경한 순서의 리스트를 재할당 
        my_reclist['my_reclist'] = my_reclist['my_reclist']+added_item
        
    return my_reclist