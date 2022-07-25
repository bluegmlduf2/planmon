import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__)) # 현재있는 파일의 디렉토리 절대경로 (SQLite저장위치지정을위해)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    # Swagger
    RESTX_MASK_SWAGGER = False
    # 게시물 이미지 임시 저장 경로와 저장된 게시물 저장경로
    POST_TEMP_FILE_PATH = basedir+'/image/posttempimage/'
    POST_FILE_PATH = basedir+'/image/postimage/'
    # 유저 이미지 저장경로
    USER_FILE_PATH = basedir+'/image/userimage/'


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'planmon_main.db') # 데이터베이스 접속주소, SQLite를 사용해서 db를 파일로 관리한다 
    SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy의 이벤트를 처리하는 옵션 (수정사항에 대한 TRACK)


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'planmon_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
