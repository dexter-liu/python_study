#!/usr/bin/env python
# -*- coding:utf-8 -*-


# r/R一个意思
# a = 'abc'
# print(a)
# print(a.encode('utf8'))

b = '''
Aasdadadadadadadadadadad
'''
# print(b.swapcase())  # 交互大小写，小写变大写，大写变小写

# lst_1 = ['1', '2', '3']
# lst = [1, 2, 3]
# print("\n".join(lst_1))

# split(sep=None, maxsplit=-1), 从左至右，maxsplit指定分割的次数，-1表示遍历整个字符串
s1 = '''I'm \ta supper student.
you are a teacher.\n'''

# print(s1.split(maxsplit=1))
# print(s1.splitlines())
# print(s1.splitlines(True))

# partition(sep) -> (head, sep, tail), sep分割字符串，必须指定
# print(s1.partition('s'))
# print(s1.rpartition('s'))
# print(s1.partition('abc'))
# print(s1.rpartition('abc'))

# find and rfind
# print(s1.rfind('tea', 31, 36))

# endswith(suffix[, start, end]), startswith
# print(s1.index('s'))
# print(s1.startswith('s', 7, 14))
print(s1.isspace())
