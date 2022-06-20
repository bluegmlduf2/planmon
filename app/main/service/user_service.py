import uuid
import datetime

from app.main import db
from app.main.model.user import User
from typing import Dict, Tuple


def get_user(uid):
    '''유저가 존재하는지 확인'''
    # 유저가 존재하면 1(True)를 반환함
    is_user=User.query.filter_by(uid=uid).count()
    return is_user

def save_user(uid):
    '''유저가 존재하지 않으면 DB에 유저 등록'''
    user = User()
    user.uid = uid
    db.session.add(user)
    db.session.commit()

################################# 여기부터 아래는 미사용 ##########################################
def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user: User) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()

