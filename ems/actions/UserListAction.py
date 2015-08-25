# coding:utf-8
from ActionBase import ActionBase
from ..models.UserDao import UserDao


class UserListAction(ActionBase):
    def __init__(self):
        ActionBase.__init__(self)

    def doGet(self):
        strGroup = ActionBase.checkArgs(self, 'group', '')

        if strGroup != '':
            arrUsers = UserDao.queryUserByGroup(strGroup)
        else:
            arrUsers = UserDao.getUserList()

        return {
            'code': 0,
            'decs': 'ok',
            'result': arrUsers
        }
