# coding:utf-8
from ..conf.Default import Config
from ..conf.ErrCode import ErrCode
from ..exception.EmsException import EmsException

from flask import session, escape, request
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

    def checkGetArgs(self, key, default_value, not_empty=False):
        if not_empty:
            value = request.args.get(key, '')
            if value == '':
                raise EmsException(ErrCode.ERR_PARAMETER_NOT_FOUND,
                                   'Parameter not found: %s' % (key))
            else:
                return value
        else:
            return request.args.get(key, default_value)

    def checkPostArgs(self, key, default_value, not_empty=False):
        if not_empty:
            value = request.form.get(key, '')
            if value == '':
                raise EmsException(ErrCode.ERR_PARAMETER_NOT_FOUND,
                                   'Parameter not found: %s' % (key))
            else:
                return value
        else:
            return request.form.get(key, default_value)

    def get(self):
        try:
            return self.doGet()
        except EmsException as e:
            return {
                'code': e.code,
                'desc': e.desc
            }
        except Exception as e:
            return {
                'code': ErrCode.ERR_UNKOWN_ERROR,
                'desc': 'Unkown error: %s' % (e),
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
            return {
                'code': ErrCode.ERR_UNKOWN_ERROR,
                'desc': 'Unkown error: %s' % (e),
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
