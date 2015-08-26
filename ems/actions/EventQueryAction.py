# coding:utf-8
from ActionBase import ActionBase
from ..models.EventDao import EventDao
from ..models.LendingDao import LendingDao


class EventQueryAction(ActionBase):
    def __init__(self):
        ActionBase.__init__(self)

    def doGet(self):
        strEventId = ActionBase.checkArgs(self, 'event_id', '', True)
        strEventId = '1'

        arrEvent = EventDao.queryEvent(int(strEventId))
        arrLendings = LendingDao.getLendingByEventId(int(strEventId))

        arrEvent['gmt_create'] = str(arrEvent['gmt_create'])
        for lending in arrLendings:
            lending['gmt_create'] = str(lending['gmt_create'])
        arrEvent['lendings'] = arrLendings

        return {
            'code': 0,
            'desc': 'ok',
            'result': arrEvent
        }
