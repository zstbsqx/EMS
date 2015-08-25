# coding:utf-8
import hashlib
from ActionBase import ActionBase
from ..models.UserDao import UserDao


class UserCreateAction(ActionBase):
    def __init__(self):
        ActionBase.__init__(self)

    def doPost(self):
        strEmail = ActionBase.checkArgs(self, 'email', '', True)
        strName = ActionBase.checkArgs(self, 'name', '', True)
        strRealName = ActionBase.checkArgs(self, 'real_name', '', True)
        strPassword = ActionBase.checkArgs(self, 'password', '', True)

        m = hashlib.md5()
        m.update(strPassword)
        strMd5Password = m.hexdigest()

        UserDao.addUser({
            'name': strName,
            'real_name': strRealName,
            'email': strEmail,
            'password': strMd5Password
        })

        return {
            'code': 0,
            'desc': 'ok'
        }
