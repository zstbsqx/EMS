from ActionBase import ActionBase
from flask import session


class LogoutAction(ActionBase):
    def doGet(self):
        if 'uid' in session:
            del session['uid']
            return 'Logout success'
        else:
            return 'You are not logged in'
