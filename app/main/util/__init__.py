from flask import current_app,request
from datetime import datetime
from sqlalchemy import case
from pytz import timezone
from uuid import uuid1
import os # 파일 이동용
import shutil # 파일 이동용
from PIL import Image  # 이미지 사이즈 변경
import random # 디폴트 이미지명 난수생성



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

def convert_string_to_date(inputDate):
    '''문자열을 데이터 형식(YYYY-MM-DD형식)으로 바꾼다'''
    # datetime.strptime(inputDate,"%Y-%m-%dT%H:%M:%S.%fZ").date().strftime("%Y-%m-%d")
    # 문자열 yyy-mm-dd'T'HH:mm:ss를 문자열 YYYY-MM-DD로 변환한 경우 
    format = '%Y-%m-%d' # YYYY-MM-DD형식
    return datetime.strptime(inputDate, format).date()

def upload_image(param):
    '''게시글 이미지 추가'''
    try:
        # 파일명변경
        time = get_current_time().strftime('%Y%m%d%H%M%S')  # 현재시간을 YYYYmmddHHMMSS 형태의 시간 출력
        ranNum = str(random.randint(1, 999999)).rjust(4, "0")  # 난수4자리,공백은0으로채움
        resize_image_fileNm = time+ranNum+".jpg"  # 변경후 저장한 파일명

        # 이미지 저장
        image = Image.open(param)
        source = current_app.config['POST_TEMP_FILE_PATH']+resize_image_fileNm  # 임시파일저장경로

        # RGB형식으로 변경후 , 이미지 파일 저장
        image.convert('RGB').save(source)  # resize사용시 image -> resize_image

        # 임시 저장된 이미지의 URL
        url = request.url+'/temp/'+resize_image_fileNm
    except Exception as e:
        raise e
    else:
        return url,resize_image_fileNm


def upload_user_image(param):
    '''유저 이미지 추가'''
    try:
        # 파일명변경
        time = get_current_time().strftime('%Y%m%d%H%M%S')  # 현재시간을 YYYYmmddHHMMSS 형태의 시간 출력
        ranNum = str(random.randint(1, 999999)).rjust(4, "0")  # 난수4자리,공백은0으로채움
        resize_image_fileNm = time+ranNum+".jpg"  # 변경후 저장한 파일명

        # 이미지 저장
        image = Image.open(param)
        resize_image_file = image.resize((160, 160)) # 160,160 이미지 사이즈변경
        source = current_app.config['USER_FILE_PATH']+resize_image_fileNm  # 유저이미지파일저장경로

        # RGB형식으로 변경후 , 이미지 파일 저장
        resize_image_file.convert('RGB').save(source)  # resize사용시 image -> resize_image

        # 저장된 이미지의 URL
        url = request.url+'/'+resize_image_fileNm
    except Exception as e:
        raise e
    else:
        return url


# 임시이미지 파일을 저장용 폴더에 이동
def moveImageFile(imageFileNames):
    # 파일 이동에 필요한 설정부분
    postTempFilePath = current_app.config['POST_TEMP_FILE_PATH'] # 게시물 임시 저장 위치
    postFilePath = current_app.config['POST_FILE_PATH'] # 게시물 저장 위치
    imageTempForder = os.listdir(postTempFilePath) # 임시파일이 위치한 폴더

    # 파일 이동 실행 부분
    for imageFile in imageTempForder:
        if imageFile in imageFileNames:
            shutil.move(postTempFilePath + imageFile, postFilePath + imageFile) # 파일이동