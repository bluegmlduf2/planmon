from .. import db

class Mylist(db.Model):
    """ 유저가 선택중인 일정 정보 취득 """
    __tablename__ = "mylist"

    myListId = db.Column(db.String(255), primary_key=True) # 다른 list 테이블의 외래키
    uid = db.Column(db.String(255), primary_key=True)
    listKind = db.Column(db.String(8), nullable=False) # todo,rec,all,complete

    def __repr__(self):
        return "<Mylist '{}'>".format(self.uid)
