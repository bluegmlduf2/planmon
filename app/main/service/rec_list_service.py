from app.main.model.list import List
from app.main.model.mylist import Mylist
from datetime import datetime
from pytz import timezone

def get_reclist(selection):
    '''유저의 할일 리스트 취득'''
    # 빈 검색조건 제외
    filters = {k: v for k, v in selection.items() if v is not None} 
    filters.pop('entryDate',None)  # 검색조건의 입국일자 존재시 제외
    filters.pop('myCompletelist',None)  # 검색조건의 완료일정 존재시 제외
    filters.pop('myTodolist',None)  # 검색조건의 할일일정 존재시 제외
    myList = [x['postId'] for x in selection['myCompletelist']]+[x['postId'] for x in selection['myTodolist']] # 검색조건으로 완료일정과 할일일정을 제외함 

    # 추천 일정 취득 (할일일정과 완료일정제외)
    my_reclist = List.query.filter_by(**filters).filter(~List.postId.in_(myList)).order_by(List.createdDate.desc()).all() 

    # 체류중인상태에서 입국후 지난 날짜의 조건이 가까운 순서로 조회
    if selection['stayStatus'] == '1' and selection['entryDate'] is not None:
        dateFormat = '%Y-%m-%d'
        entryDate = datetime.strptime(selection['entryDate'],dateFormat) # 입국날짜
        currentDate = datetime.strptime(datetime.now(timezone('Asia/Seoul')).strftime(dateFormat),dateFormat) # 현재시간
        # 만약 입국날짜가 현재시간보다 미래일 경우 일반 추천 일정반환
        if currentDate < entryDate:
            return my_reclist
        diff = (currentDate-entryDate).days # 입국후 경과 일수
        # 사용자에게 유효한 추천일정을 상위에 표시한다
        # 아래의 로직은 일정의 인덱스 위치를 변경하는 로직
        added_item = []
        deleted_item = []
        for x in my_reclist:
            # 사용자의 입국후 일자와 작성자의 입국후 일정시작 일자를 비교해서 유효한 리스트를 상위에 표시한다
            if diff > x.afterEntryDate:
                added_item.append(x)
                deleted_item.append(x)
        # 삭제한 아이템을 추천일정으로부터 삭제하기
        for x in deleted_item:
            my_reclist.remove(x)
        # 변경한 순서의 리스트를 재할당 
        my_reclist = my_reclist+added_item
        
    return my_reclist