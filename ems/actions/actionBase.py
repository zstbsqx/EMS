# coding:utf-8
from ..conf.default import Config
from ..conf.errCode import ErrCode
from ..exception.emsException import EmsException

from flask import session, escape
from flask_restful import Resource


class ActionBase(Resource):
    def __init__(self):
        pass

    def checkUserLogin(self):
        if Config.CHECK_USER_LOGIN == 0:
            return True
        elif 'username' not in session:
            raise EmsException(ErrCode.ERR_USER_NOT_LOGIN, 'User not login')
            return False
        return True

    def getUserName(self):
        if 'username' in session:
            return escape(session['username'])
        return ''

    def get(self):
        try:
            return self.doGet()
        except EmsException as e:
            return {
                'code': e.code,
                'desc': e.desc
            }
        except Exception as e:
            pass
        return {
            'code': ErrCode.UNKOWN_ERROR,
            'desc': 'unkown error',
        }

    def post(self):
        try:
            return self.doPost()
        except EmsException as e:
            return {
                'code': e.code,
                'desc': e.desc
            }
        except Exception as e:
            pass
        return {
            'code': ErrCode.UNKOWN_ERROR,
            'desc': 'unkown error',
        }

    def doPost(self):
        return {
            'code': ErrCode.ERR_ACTION_POST_NOT_DEFINE,
            'desc': 'The post action is not define'
        }

    def doGet(self):
        return {
            'code': ErrCode.ERR_ACTION_GET_NOT_DEFINE,
            'desc': 'The get action is not define'
        }
