from functools import wraps
from flask import request,abort
from app.main.service.auth_helper import Auth
from app.main.service.user_service import get_user,save_user
from app.main.util import UserError, getMessage, get_uuid
from typing import Callable
import logging

def token_required(f) -> Callable:
    '''토큰에 유저정보가 존재 필수, uid반환'''
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.check_verified_user(request)
        token = data.get('Authorization') # 인증여부
        uid =data.get('uid') # uid

        # 인증정보가 존재하지 않을 시 
        if not token:
            return abort(401,'해당 요청에 대한 권한이 없습니다')
        
        # 인증되었지만 DB에 유저정보가 없을시 DB에 유저ID 등록
        if not get_user(uid):
            save_user(uid)

        # 인증이 문제없으면 진행
        return f(uid ,*args, **kwargs)

    return decorated

def get_user_by_token(f) -> Callable:
    '''토큰에 유저정보가 존재 필수가아님, uid반환'''
    @wraps(f)
    def decorated(*args, **kwargs):

        data = Auth.check_verified_user(request)[0]
        uid =data.get('uid') # uid
        
        # 인증되었지만 DB에 유저정보가 없을시 DB에 유저ID 등록
        if uid:
            if not get_user(uid):
                save_user(uid)

        # 인증이 문제없으면 진행
        return f(uid ,*args, **kwargs)

    return decorated


def exception_handler(f) -> Callable:
    '''에러핸들링'''
    @wraps(f)  # f.doc 과 같은 값을 잃어버리지 않도록 설정
    def decorated(*args, **kwargs):
        try:
            # 로그설정 (INFO까지표시)
            logging.basicConfig(
                format=f'#----- [%(asctime)s] [%(levelname)s] | %(message)s -----#',
                level=logging.INFO)
            
            # 로그고유번호용 UUID 
            uuid=get_uuid()

            # 사용자 IP
            user_ip=request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)

            # 로그 기록
            logging.info(f"[ {uuid} ] 컨트롤러 메소드 시작 => ("+f.__qualname__+")")
            logging.info(f"[ {uuid} ] 접속자 IP주소        => ("+user_ip+")")
            result = f(*args, **kwargs)  # 인자로 전달받은 f 호출 / result는 f()의 반환값            
            logging.info(f"[ {uuid} ] 컨트롤러 메소드 종료 => ("+f.__qualname__+")")
        except UserError as e:
            # 사용자에러 처리
            return e.errorInfo,400
        except Exception as e:
            # 기타 예외 처리
            logging.exception(e)
            return getMessage(801),500
        else:
            # 성공적으로 반환된 값 전달
            return result
    return decorated
