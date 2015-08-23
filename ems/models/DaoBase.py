import MySQLdb
import MySQLdb.cursors
from ..conf.Default import Config
from ..conf.ErrCode import ErrCode
from ..exception.EmsException import EmsException


class DaoBase:
    db = MySQLdb.connect(
        host=Config.DATABASE_HOST,
        port=Config.DATABASE_PORT,
        user=Config.DATABASE_USER,
        passwd=Config.DATABASE_PASSWORD,
        db=Config.DATABASE_NAME,
        cursorclass=MySQLdb.cursors.DictCursor,
        charset='utf8')

    @classmethod
    def get(cls, columnList=['*'], conditions=None):
        with cls.db as cursor:
            columns = ','.join(columnList) if len(columnList) > 0 else '*'
            sql = 'SELECT ' + columns + ' FROM ' + cls.table
            if conditions:
                sql += ' ' + conditions
            try:
                cursor.execute(sql)
                header = cursor.description
                rows = cursor.fetchall()
                result = []
                for row in rows:
                    obj = {}
                    for i in xrange(len(header)):
                        obj[header[i][0]] = row[i]
                    result.append(obj)
                return obj
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED,
                                   'Query db failed')

    @classmethod
    def insert(cls, obj):
        with cls.db as cursor:
            columns = []
            values = []
            for key in obj:
                columns.push(key)
                values.push(obj[key])
            sql = 'INSERT INTO ' + cls.table + '(' + columns.join(',') + ') VALUES(' + values.join(',') + ')'
            try:
                count = cursor.execute(sql)
                connect.commit()
                result = {
                    "id": cursor.lastrowid,
                    "count": count
                }
                return result
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED,
                                   'Insert db failed')

    @classmethod
    def insertMany(cls, list):
        with cls.db as cursor:
            columns = []
            values = []
            template = []
            for key in list[0]:
                columns.append(key)
                template.append('%s')
            for obj in list:
                value = []
                for column in columns:
                    value.append(obj[column])
                values.append(value)
            sql = 'INSERT INTO ' + cls.table + '(' + columns.join(',') + ') VALUES(' + template.join(',') + ')'
            try:
                count = cursor.executemany(sql, values)
                connect.commit()
                result = {
                    "count": count
                }
                return result
            except:
                raise EmsException(ErrCode.ERR_DB_FAILED,
                                   'Query db failed')

    @classmethod
    def update(cls, obj, conditions):
        with cls.db as cursor:
            columns = []
            for key in obj:
                columns.push(key + '=' + obj[key])
            sql = 'UPDATE ' + cls.table + ' SET ' + columns.join(',') + ' ' + conditions
            try:
                count = cursor.execute(sql)
                connect.commit()
                result = {
                    "id": cursor.lastrowid,
                    "count": count
                }
                return result
            except:
                return {"error": "update failed"}

    @classmethod
    def updateMany(cls, list, conditions):
        with cls.db as cursor:
            columns = []
            values = []
            for key in list[0]:
                columns.push(key + '=%s')
            for obj in list:
                value = []
                for column in KVs:
                    value.append(obj[column])
                values.append(value)
            sql = 'UPDATE ' + cls.table + ' SET ' + columns.join(',') + ' ' + conditions
            try:
                count = cursor.executemany(sql, values)
                connect.commit()
                result = {
                    "count": count
                }
                return result
            except:
                return {"error": "updatemany failed"}

    @classmethod
    def delete(cls, conditions):
        with cls.db as cursor:
            sql = 'DELETE FROM ' + cls.table + ' ' + conditions
            try:
                count = cursor.execute(sql)
                result = {
                    "count": count
                }
                return result
            except:
                return {"error": "delete failed"}
