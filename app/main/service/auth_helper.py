from app.main.model.user import User
from ..service.blacklist_service import save_token
from typing import Dict, Tuple
from firebase_admin import auth # 파이어베이스 인증모듈

class Auth:

    @staticmethod
    def check_verified_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        '''인증 유저 확인 '''
        try:
            auth_token= data.headers.get('authorization')
            if auth_token:
                try:
                    # 파이어베이스에서 유저정보인증 확인
                    user = auth.verify_id_token(auth_token.replace("Bearer ",""))
                    response_object = {
                        'status': 'success',
                        'message': '성공적으로 인증되었습니다',
                        'Authorization': True,
                        'uid': user.get('uid'),
                    }
                    return response_object, 200
                except:
                    #유효하지않은 토큰
                    response_object = {
                        'status': 'fail',
                        'message': '유효하지않은 토큰입니다'
                    }
                    return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': '인증정보가 존재하지않습니다'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': '인증진행중 시스템에러 발생'
            }
            return response_object, 500

    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = User.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
