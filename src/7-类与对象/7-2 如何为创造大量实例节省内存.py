#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 03:06:31 2018

@author: yahkun
"""

'''
实际案例:
    某网络游戏中, 定义了玩家类 Player(id, names, status, ...)每有一个在线玩家, 在服务器
程序中则有一个 Player 的实例, 当在线人数很多时, 将产生大量实例(如百万级)

如何降低这些大量实力的内存开销?
'''

'''
解决方案:
    定义类的__slot__属性, 它是用来声明实例属性名字的列表
'''

class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

class Player2(object):
    __slots__ = ['uid', 'name', 'status', 'level']  # 提前定义对象属性
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

p1 = Player('0001', 'Jim')
p2 = Player2('0001', 'Jim')

print(set(dir(p1)) - set(dir(p2)))
# p1.__dict__ 实现动态绑定属性是以牺牲内存为代价的