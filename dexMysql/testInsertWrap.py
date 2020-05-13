#!/usr/bin/env python
# -*- coding:utf-8 -*-


from dexMysql.dexMysqlHelper import MysqlHelper

sql = 'INSERT INTO STU(name,gender) VALUES(%s,%s)'
name = input('请输入学生姓名：')
gender = input('请输入学生性别, 1为男, 0为女: ')
params = (name, gender)

tmp_mysql = MysqlHelper('192.168.56.103', 'dexter', 'dexter', 'TESTDB')
count = tmp_mysql.insert(sql, params)
if count == 1:
    print('insert into successfully')
else:
    print('failed')






