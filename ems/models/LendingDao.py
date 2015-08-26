# coding: utf-8
from DaoBase import DaoBase
from ..conf.Default import Config
from ..conf.ErrCode import ErrCode
from ..exception.EmsException import EmsException


class LendingDao(DaoBase):
    table = Config.TABLE_LENDINGS

    @classmethod
    def getLendingByEventId(cls, intEventId):
        with DaoBase.db as cursor:
            sql = "SELECT * FROM %s where event_id = %d" \
                % (Config.TABLE_LENDINGS, intEventId)
            try:
                cursor.execute(sql)
                return cursor.fetchall()
            except:
                return EmsException(ErrCode.ERR_DB_FAILED, 'Query db failed')
