from .ActionBase import ActionBase
from ..models import UserDao
from flask import request


class Test(ActionBase):
    def __init__(self):
        ActionBase.__init__(self)

    def doGet(self):
        ActionBase.checkUserLogin(self)

        strUser = ActionBase.getUserName(self)
        arrUser = models.User.get()

        return {
            'code': 0,
            'desc': 'ok',
            'user': strUser,
            'result': arrUser
        }
