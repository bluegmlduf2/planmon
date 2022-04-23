import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist

# main디렉토리에 있는 사용자 환경설정 끝난 플라스크 앱 초기화
app = create_app(os.getenv('SERVER_ENV') or 'dev') # dev, prod, test 중에 동작 (기본 dev)
app.register_blueprint(blueprint)

app.app_context().push()

# flask_script사용 등록
# 파이선 스크립트 실행 명령어등을 사용자 지정가능
# @manager.command def run() -> manager.run() -> python3 manage.py run
manager = Manager(app) 

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    # 플라스크 앱 기동
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
