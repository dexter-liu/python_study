#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 集合，类似于dict，只不过不存储value，创建空集合使用set(),而不能使用{}
s = {'i', 'love', 'yao', 'qian'}
s.update(['yeah'])
print(s)
p_p = s.pop()
print(p_p)
tup = (1, 2, 3)
s.add(tup)
s.add(tup)
s.discard('i')
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 - s2)
print(s1 ^ s2)
print(s1 & s1)
print(s1 | s2)