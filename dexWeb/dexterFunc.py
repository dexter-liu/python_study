#!/usr/bin/env python
'''
# list and dict 作为全局变量，在函数中可以不用global申明
# example

# 拆包， 元祖和字典
# example
def testDexter(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
A = (44, 55, 66)
B = {"name":"qian", "age":18}

# *A, **B 拆包
testDexter(11, 22, 33, *A, **B)
'''

# 递归函数
def getNums(num):
    if num > 1:
        return num * getNums(num - 1)
    else:
        return num # 一定要想清楚什么时候递归结束，不调用了
result = getNums(5)
print(result)
B = {"name":"qian", "age":18}
A = [44, 55, 66]
A.sort()


