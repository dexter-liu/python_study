#!/usr/bin/env python
# -*- coding:utf-8 -*-


# tuple比list占用空间更小
# t = (1, 2, 3) * 5
# print(t)

# namedtuple
# 命名元祖，返回一个元祖的子类，并定义了字段，field_names可以是空格或逗号分割的字段的字符串，可以是字段的列表
# namedtuple(typename, field_names, vervose=False, rename=False)
'''
from collections import namedtuple
Point = namedtuple('_Point', ['x', 'y'])
p = Point(11, 22)
print(type(p))
print(p)

student = namedtuple('Student', 'name age')
tom = student('tom', 20)
print(tom)
print(type(tom))
print(tom.name)
'''

# nums = []
# for i in range(5):
#     nums.append(int(input('%d: ' % i)))
# print(nums)
# nums.sort(reverse=True)
# print(nums)


# 冒泡法，交换排序
num_list = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 9, 8]
]
nums = num_list[2]
print(nums)
length = len(nums)
count_swap = 0
count = 0
for i in range(length):
    flag = False  # 优化点
    for j in range(length - 1 - i):  # 外层循环进入的时候需要减去i
        count += 1
        if nums[j] > nums[j + 1]:
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp
            flag = True
            count_swap += 1
    if not flag:
        break


print(nums, count_swap, count)

