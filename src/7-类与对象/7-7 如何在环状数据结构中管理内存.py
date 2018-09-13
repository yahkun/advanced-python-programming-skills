#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 05:24:29 2018

@author: yahkun
"""

'''
实际案例:
    在 Python 中, 垃圾回收器通过引用计数来回收垃圾对象, 但某些环状数据结构(树, 图...), 存
在对象间的循环引用, 比如树的父节点引用子节点, 子节点也同时引用父节点. 此时同时 del 掉引用父子
节点, 两个对象不能被立即回收.

如何解决此类的内存管理问题?
'''

'''
解决方案:
    使用标准库 weakref, 他可以创建一种能访问对象但不增加引用计数的对象
'''
import weakref


#class Data(object):
#    def __init__(self, value, owner):
#        self.value = value
#        self.owner = owner
#    
#    def __str__(self):
#        return f'{self.owner}\'s data, value is {self.value}'
#    
#    def __del__(self):
#        print('in Data.__del__')
#
#class Node(object):
#    def __init__(self, value):
#        self.data = Data(value, self)
#    
#    def __del__(self):
#        print('in Node.__del__')


class Data(object):
    def __init__(self, value, owner):
        self.value = value
        self.owner = weakref.ref(owner)
    
    def __str__(self):
        return f'{self.owner()}\'s data, value is {self.value}'
    
    def __del__(self):
        print('in Data.__del__')

class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)
    
    def __del__(self):
        print('in Node.__del__')
        
        
node = Node(100)
del node    # 没有输出
input('Wait...')


