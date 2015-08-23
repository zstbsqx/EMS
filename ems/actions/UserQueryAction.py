# coding:utf-8
from ActionBase import ActionBase
from ..models.UserDao import UserDao


class UserQueryAction(ActionBase):
    def __init__(self):
        ActionBase.__init__(self)

    def doGet(self):
        strId = ActionBase.checkGetArgs(self, 'id', '', True)
        dictUser = UserDao.queryUser(strId)

        return {
            'code': 0,
            'desc': 'ok',
            'result': dictUser
        }
