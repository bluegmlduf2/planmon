from flask_restx import Api # REST API구현
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__) # __name__는 현재 모듈이다. 여기선 디렉토리 app이다. 이것을 Bluepirnt에 등록
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

# flask_restx
# flask-restful의 라이브러리
# Swagger라는 rest api를 문서화해주는 도구를 지원
api = Api(
    blueprint,
    title='FLASK RESTPLUS(RESTX) API PLANMON WITH JWT',
    version='1.0',
    description='PLANMON for flask restplus (restx) web service',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
