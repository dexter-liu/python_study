#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys


class DexterClass1(object):
    _name1 = 'dog_name1'
    __name2 = 'dog_name2'

    def __init__(self):
        pass

    def set_age(self, new_age):
        if 0 < new_age <= 100:
            self.age = new_age
        else:
            self.age = 0

    def get_age(self):
        return self.age

    def get_name(self):
        return self.__name2

    def __cry(self):
        print('dog is cry out')

    def cry(self):
        self.__cry()

    def __del__(self):
        print('------------英雄over-----------')


class DexterClass2(DexterClass1):
    # pass
    
    def get_name(self):
        # return self._name1
        return DexterClass1.get_name(self)  # or super().get_name()


def main():
    dog = DexterClass2()
    dog.set_age(10)
    print(dog.get_age())
    # print(dog._name1)
    # print(dog.__name2)
    print(dog.get_name())
    print(dog.cry())
    # dog1 = DexterClass1()
    # dog2 = dog1
    # print(sys.getrefcount(dog1))  # 测量一个对象引用次数的方式
    # del dog1
    # print('=' * 50)
    # # 执行完程序退出，对象会被调用__del__方法，回收
    print(DexterClass2.__mro__)  # C3算法


if __name__ == '__main__':
    main()
