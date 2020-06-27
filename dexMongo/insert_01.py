#!/usr/bin/env python
# -*- coding:utf-8 -*-


import pymongo

# 连接， 创建客户端
# cli = pymongo.MongoClient('192.168.56.103', 27017)
cli = pymongo.MongoClient('mongodb://admin:2019Nov!@192.168.56.103:27017/admin')

dblist = cli.list_database_names()
# for db in dblist:
#     print('%s 数据库已存在' % db)
# 获得数据库py3
db = cli.py3

# 查找数据库下面的集合列表
# for col in db.list_collection_names():
#     print('%s 集合已经存在' % col)

# 获得集合
stu = db.stu

# 添加文档
# s1 = {'name': 'test1', 'age': 18, 'gender': 1}
# s1_id = stu.insert_one(s1).inserted_id
# print(s1_id)

# 添加多行数据
# s_many = [
#     {'name': 'test2', 'age': 19, 'gender': 1},
#     {'name': 'test3', 'age': 20, 'gender': 1},
#     {'name': 'test4', 'age': 21, 'gender': 1}
# ]
# print(stu.insert_many(s_many))
# # s_many_id = stu.insert_many(s_many).inserted_ids
# # print(s_many_id)

mylist = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google 搜索"},
    {"_id": 3, "name": "Facebook", "address": "脸书"},
    {"_id": 4, "name": "Taobao", "address": "淘宝"},
    {"_id": 5, "name": "Zhihu", "address": "知乎"}
]
x = stu.insert_many(mylist)
print(x.inserted_ids)
