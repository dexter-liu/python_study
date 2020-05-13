#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dexMysqlHelper import MysqlHelper
import hashlib


name = input('请输入用户名: ')
passwd = input('请输入密码: ')

s1 = hashlib.sha1()
# s1.update(passwd.encode('utf-8'))
s1.update(bytes(passwd, encoding='utf-8'))
spwdsha1 = s1.hexdigest()
print(spwdsha1)

# 根据用户名查询
sql = 'SELECT upwd FROM userinfos WHERE uname=%s'
params = (name,)

sqlhelper = MysqlHelper(host='192.168.56.103', user='dexter', password='dexter', database='TESTDB')
userinfo = sqlhelper.get_one(sql, params)

if userinfo == None:
    print('user is not exist')
elif userinfo[0] == spwdsha1:
    print('login successfully')
else:
    print('password is not correct')





