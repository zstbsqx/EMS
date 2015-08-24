# coding: utf-8
# author: winton
from DaoBase import DaoBase
from ..conf.Default import Config
from ..conf.ErrCode import ErrCode
from ..exception.EmsException import EmsException


class UserDao(DaoBase):
    table = Config.TABLE_USERS

    @classmethod
    def addUser(cls, dictUser):
        with DaoBase.db as cursor:
            sql = "INSERT INTO %s(name,real_name,email,password) \
                VALUE(%s,%s,%s,%s)" \
                % (Config.TABLE_USERS,
                   dictUser['name'],
                   dictUser['real_name'],
                   dictUser['email'],
                   dictUser['password'])
            try:
                cursor.execute(sql)
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED, 'Insert db failed')

    @classmethod
    def queryUser(cls, strId):
        with DaoBase.db as cursor:
            sql = "SELECT user_id,name,real_name,email,group FROM %s WHERE id = %d" \
                % (Config.TABLE_USERS, int(strId))
            try:
                cursor.execute(sql)
                return cursor.fetchone()
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED, 'Query db failed')
