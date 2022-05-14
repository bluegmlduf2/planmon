from app.main.model.user import User


def get_a_selection(uid):
    user=User.query.filter_by(uid=uid).first()
    return user