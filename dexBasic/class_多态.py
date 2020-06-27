#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Dog(object):
    def print_self(self):
        print('大家好，我是xxx')


class XaioDog(Dog):
    def print_self(self):
        print('hello everybody, 我是你们的老大')


def introduce(temp):
    temp.print_self()


dog1 = Dog()
dog2 = XaioDog()

introduce(dog1)
introduce(dog2)