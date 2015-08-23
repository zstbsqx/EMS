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
        DaoBase.insert(dictUser)

    @classmethod
    def queryUser(cls, strId):
        cursor = DaoBase.db.cursor()
        sql = "SELECT id,name,email FROM %s WHERE id = %d" \
            % (Config.TABLE_USERS, int(strId))
        try:
            cursor.execute(sql)
            return cursor.fetchone()
        except:
            raise EmsException(ErrCode.ERR_DB_FAILED, 'Query db failed')
