#!/usr/bin/env python
# -*- coding:utf-8 -*-


import math
import datetime

n = 10000
pn = []
flag = False
count = 0
start = datetime.datetime.now()
for x in range(2, n):
    for i in pn:
        count += 1
        if x % i == 0:
            flag = True
            break
        if i >= math.ceil(x ** 5):
            flag = False
            break
    if not flag:
        pn.append(x)
delta = (datetime.datetime.now() - start).total_seconds()
print(len(pn))
print(count)
print(delta)
print(pn)