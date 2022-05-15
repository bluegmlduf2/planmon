from .. import db
import datetime
from pytz import timezone
from uuid import uuid1

class List(db.Model):
    """ 리스트정보 취득 """
    __tablename__ = "list"

    postId = db.Column(db.String(255), primary_key=True)
    writerUid = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    createdDate = db.Column(db.DateTime, nullable=False)
    updatedDate = db.Column(db.DateTime, nullable=False)

    def __init__(self):
        self.postId = uuid1() # 시스템의 현재시간과 호스트ID 기반으로 UUID 생성
        current_date_time = datetime.datetime.now(timezone('Asia/Seoul')) # 한국기준 시간
        self.createdDate = current_date_time # 작성시간 초기화
        self.updatedDate = current_date_time # 수정시간 초기화

    def __repr__(self):
        return "<List '{}'>".format(self.postId)