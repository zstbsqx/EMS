import MySQLdb
import conf

db = MySQLdb.connect(host=conf.DATABASE_HOST, port=conf.DATABASE_PORT, user=conf.DATABASE_USER, passwd=conf.DATABASE_PASSWORD, db=conf.DATABASE_NAME)

class Model:

    @classmethod
    def get(cls, columnList=['*'], conditions=None):
        with db as cursor:
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
                return {"error": "get failed"}

    @classmethod
    def insert(cls, obj):
        with db as cursor:
            columns = []
            values = []
            for key in obj:
                columns.push(key)
                values.push(obj[key])
            sql = 'INSERT INTO ' + cls.table + '(' + columns.join(',') + ') VALUES(' + values.join(',') + ')'
            try:
                count = cursor.execute(sql)
                connect.commit()
                id = cursor.lastrowid
                result = {
                    "id": cursor.lastrowid, 
                    "count": count
                }
                return result
            except:
                return {"error": "insert failed"}

    @classmethod
    def insertMany(cls, list):
        with db as cursor:
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
                return {"error": "insertMany failed"}



    @classmethod
    def update(cls, obj, conditions):
        with db as cursor:
            columns = []
            for key in obj:
                columns.push(key + '=' + obj[key])
            sql = 'UPDATE ' + cls.table + ' SET ' + columns.join(',') + ' ' + conditions
            try:
                count = cursor.execute(sql)
                connect.commit()
                id = cursor.lastrowid
                result = {
                    "id": cursor.lastrowid, 
                    "count": count
                }
                return result
            except:
                return {"error": "update failed"}

    @classmethod
    def updateMany(cls, list, conditions):
        with db as cursor:
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
        with db as cursor:
            sql = 'DELETE FROM ' + cls.table + ' ' + conditions
            try:
                count = cursor.execute(sql)
                result = {
                    "count": count
                }
                return result
            except:
                return {"error": "delete failed"}

class User(Model):
    table = 'users'

class Event(Model):
    table = 'events'

class Lending(Model):
    table = 'lendings'

if __name__ == '__main__':
    print User.get()
