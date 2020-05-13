#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 安装mysql-connector库会报authentication error with authentication plugin 'calling_sha2_password' is not supported
import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.56.103",
    user="dexter",
    passwd="dexter"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="123456",
#     database="runoob_db"
# )
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
#
# print(mycursor.rowcount, "记录插入成功。")
#
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="123456",
#     database="runoob_db"
# )
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("Zhihu", "https://www.zhihu.com")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print("1 条记录已插入, ID:", mycursor.lastrowid)

