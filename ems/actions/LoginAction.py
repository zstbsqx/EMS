from ActionBase import ActionBase
from flask import request, session
from hashlib import md5


class LoginAction(ActionBase):
    def doPost(self):
        #
        hashedPassword = md5()
