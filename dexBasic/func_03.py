#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)

# import datetime, time
# print(datetime.datetime.now())
# print(time.time())

# 函数执行流程，压栈（常量、变量也需要压栈），栈帧(call function)，出栈，恢复现场，函数上下文（内存分为栈内存，堆内存），循环不需要压栈

# def foo1(b, b1=3):
#     print('foo1 called', b, b1)
#
# def foo2(c):
#     foo3(c)
#     print('foo2 called', c)
#
# def foo3(d):
#     print('foo3 called', d)
#
# def main():
#     print('main called')
#     foo1(100, 101)
#     foo2(200)
#     print('main ending')
#
#
# main()


# 斐波那契数列实现
# pre = 0
# cur = 1
# print(pre, cur, end=' ')
#
#
# def fib(n, pre=0, cur=1):  # recursion
#     pre, cur = cur, pre + cur
#     print(cur, end=' ')
#     if n == 2:
#         return
#     fib(n - 1, pre, cur)
#
#
# fib(5)

# num = 1234
#
#
# def revert(num, target=[]):
#     if num:
#         target.append(num[-1:])
#         revert(num[:len(num) - 1])
#     return target
#
#
# print(revert(str(num)))

# 猴子吃桃问题