# coding: utf-8
from ActionBase import ActionBase
from ..models.EventDao import EventDao


class EventListAction(ActionBase):
    def __init__(self):
        ActionBase.__init__(self)

    def doGet(self):
        strPage = ActionBase.checkArgs(self, 'page', '0')
        strPageSize = ActionBase.checkArgs(self, 'page_size', '25')

        arrEvents = EventDao.getEventList(int(strPage), int(strPageSize))

        for event in arrEvents:
            event['gmt_create'] = str(event['gmt_create'])

        return {
            'code': 0,
            'desc': 'ok',
            'result': arrEvents
        }
