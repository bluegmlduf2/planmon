def sort_by_id(ids,list):
    '''매개변수로 전달된 리스트의 순서를 postIds의 순서에 맞춰 변경한다'''
    sorted_list= [] # 정렬된 배열순서
    for x in ids:
        for y in list:
            if x == y.postId:
                sorted_list.append(y)
    return sorted_list