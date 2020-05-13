#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dexMysqlHelper import MysqlHelper

sql = 'SELECT * FROM STU ORDER BY id desc'
# name = input('请输入学生姓名：')
# params = (name,)

tmp_mysql = MysqlHelper('192.168.56.103', 'dexter', 'dexter', 'TESTDB')
one = tmp_mysql.get_all(sql)
for x in one:
    print(x)
