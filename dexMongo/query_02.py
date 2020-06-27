#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymongo


cli = pymongo.MongoClient('mongodb://admin:2019Nov!@192.168.56.103:27017/admin')
db = cli['py3']
stu = db['stu']

# 查询一条数据
# x = stu.find_one()
# print(x)

# 查询指定的字段key
# for x in stu.find({}, {"_id": 0, 'name': 1}):
#     print(x)

# 设置过滤条件
fi_1 = {'name': 'lxc'}
fi_2 = {'age': {'$gte': 30}}
fi_3 = {'name': {'$regex': '^t'}}
for x in stu.find(fi_1):
    print(x)
for x in stu.find(fi_1).limit(3):
    print(x)