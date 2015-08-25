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
                VALUE('%s','%s','%s','%s')" \
                % (Config.TABLE_USERS,
                   dictUser['name'],
                   dictUser['real_name'],
                   dictUser['email'],
                   dictUser['password'])
            try:
                cursor.execute(sql)
            except Exception as e:
                raise EmsException(ErrCode.ERR_DB_FAILED,
                                   'Insert db failed: %s' % e)

    @classmethod
    def queryUser(cls, strId):
        with DaoBase.db as cursor:
            sql = "SELECT user_id,name,real_name,email,groups FROM %s WHERE user_id = %d" \
                % (Config.TABLE_USERS, int(strId))
            try:
                cursor.execute(sql)
                return cursor.fetchone()
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED, 'Query db failed')

    @classmethod
    def queryUserByGroup(cls, strGroup):
        with DaoBase.db as cursor:
            sql = "SELECT user_id,name,real_name,email,groups FROM %s \
                WHERE groups = '%s'" \
                % (Config.TABLE_USERS, strGroup)
            try:
                cursor.execute(sql)
                return cursor.fetchall()
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED, 'Query db failed')

    @classmethod
    def getUserList(cls):
        with DaoBase.db as cursor:
            sql = "SELECT user_id,name,real_name,email,groups FROM %s" \
                % (Config.TABLE_USERS)
            try:
                cursor.execute(sql)
                return cursor.fetchall()
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED, 'Query db failed')
