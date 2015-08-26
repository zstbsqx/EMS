from ActionBase import ActionBase
from ..models import UserDao
from flask import session
import hashlib


class LoginAction(ActionBase):
    def doPost(self):
        if 'uid' in session:
            return 'You have logged in'
        name = self.checkForm('name', not_empty=True)
        password = self.checkForm('password', not_empty=True)
        print('name:%s password:%s' % (name, password))
        m = hashlib.md5()
        m.update(password)
        md5Password = m.hexdigest()
        users = UserDao.UserDao.queryLoginUser(name, md5Password)
        if len(users) is 1:
            print(users[0])
            uid = users[0]['user_id']
            session['uid'] = uid
            return 'Login success'
        else:
            return 'Login failed'
