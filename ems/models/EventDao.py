# coding: utf-8
from DaoBase import DaoBase
from ..conf.Default import Config
from ..conf.ErrCode import ErrCode
from ..exception.EmsException import EmsException


class EventDao(DaoBase):
    table = Config.TABLE_EVENTS

    @classmethod
    def getEventList(cls, page, page_size):
        with DaoBase.db as cursor:
            sql = "SELECT * FROM %s order by '%s' desc LIMIT %d, %d" \
                % (Config.TABLE_EVENTS, 'gmt_create',
                    page * page_size, page_size)
            try:
                cursor.execute(sql)
                return cursor.fetchall()
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED, 'Query db failed')

    @classmethod
    def queryEvent(cls, intEventId):
        with DaoBase.db as cursor:
            sql = "SELECT * FROM %s WHERE event_id = %d" \
                % (Config.TABLE_EVENTS, intEventId)
            try:
                cursor.execute(sql)
                return cursor.fetchone()
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED, 'Query db failed')
