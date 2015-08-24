from ActionBase import ActionBase
from flask import session
import json


class LogoutAction(ActionBase):
    def doGet(self):
        session['bug'] = 'name'
        return json.dumps(session)
