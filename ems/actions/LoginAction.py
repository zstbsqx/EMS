from ActionBase import ActionBase
from ..model import UserDao
from flask import session
from hashlib import md5


class LoginAction(ActionBase):
    def doPost(self):
        name = self.checkPostArgs('name')
        password = self.checkPostArgs('password')
        hashedPassword = md5().update(password).hexdigest()
        users = UserDao.UserDao.queryUserLogin(name, hashedPassword)
        if users:
            print(users[0])
            uid = users[0]['user_id']
            session['uid'] = uid
            return 'Login success'
        else:
            return 'Login failed'
