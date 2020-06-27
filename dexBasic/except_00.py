#!/usr/bin/env python
# -*- coding:utf-8 -*-


# try:
#     '2' + 2
# except (TypeError, NameError, RuntimeError):
#     raise


# Exception 是所有异常类的父类，使用raise抛出异常时，必须指定一个异常的实例或者是异常的子类（Exception的子类）
# 或者是简单的raise，如果只想知道这是否抛出了异常，并不想去处理它
# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

#
# try:
#     raise NameError('hi there')
# except NameError:
#     print('An exception flew by!')
#     raise

# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
#
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occured, value: ', e.value)


# 定义清理行为，如果一个异常在try子句里（或者在except和else子句里）被抛出，而又没有任何的except把它截住，那么这个异常会在finally子句执行后被抛出
# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")
#
#
# divide(2, '1')


# 预定义清理行为，使用with
with open("myfile.txt") as f:
    for line in f:
        # print(line, end="")
        print(line)
