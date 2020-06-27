#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Game(object):

    num = 0

    def __init__(self):
        self.name = "laowang"

    @classmethod
    def add_num(cls):
        cls.num = 100

    @staticmethod
    def print_menu():
        print('-'*50)
        print('穿越火线v11.1')
        print('开始游戏')
        print('结束游戏')


game = Game()
Game.add_num()  # 可以通过类调用类方法
# game.add_num()
print(Game.num)
# print(Game.print_menu())
print(game.print_menu())