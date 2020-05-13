#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql


class MysqlHelper():
    def __init__(self, host, user, password, database, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database, charset=self.charset)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cur.execute(sql, params)
            result = self.cur.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    def get_all(self, sql, params=()):
        li = ()
        try:
            self.connect()
            self.cur.execute(sql, params)
            li = self.cur.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return li

    def insert(self, sql, params):
        return self.__edit(sql, params)

    def delete(self, sql, params):
        return self.__edit(sql, params)

    def update(self, sql, params):
        return self.__edit(sql, params)

    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cur.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return count


if __name__ == '__main__':
    tmp_mysql = MysqlHelper('192.168.56.103', 'dexter', 'dexter', 'TESTDB')
    sql = 'SELECT * FROM STU'
    result = tmp_mysql.get_one(sql)
    print(result)
