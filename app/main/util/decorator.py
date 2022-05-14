from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth
from typing import Callable


def token_required(f) -> Callable:
    '''유저인증확인'''
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.check_verified_user(request)
        token = data.get('Authorization') # 인증여부
        uid =data.get('uid') # uid

        # 인증정보가 존재하지 않을 시 
        if not token:
            return data, status
        
        # 인증이 문제없으면 진행
        return f(uid ,*args, **kwargs)

    return decorated


def admin_token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated
