from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_all(self):        
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)

        self.session.add(ent)
        self.session.commit()
        self.session.close()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)

        self.session.delete(user)
        self.session.commit()
        self.session.close()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.username = user_d.get("username")
        user.password = user_d.get("password")
        user.role = user_d.get("role")

        self.session.add(user)
        self.session.commit()
        self.session.close()

    def update_partial(self, user):
        self.session.add(user)
        self.session.commit()
        self.session.close()

        return user

    def get_user_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()
