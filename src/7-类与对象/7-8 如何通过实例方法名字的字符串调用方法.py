#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 09:51:12 2018

@author: yahkun
"""

'''
实际案例:
    某项目中, 我们的代码使用了三个不同库中的图形类:
        Circle, Triangle, Rectangle
    他们都有一个获取图形面积的接口(方法), 但接口名字不同. 我们可以实现一个统一的获取面积的函
数, 使用每种方法名进行尝试, 调用相应类的接口.
'''

'''
解决方案:
    方案一:使用内置函数 getattr, 通过名字在实例上获取方法对象, 然后调用
    方案二:使用标准库 operator 下的 methodcaller 函数调用
'''
from operator import methodcaller

from lib1 import Circle
from lib2 import Triangle
from lib3 import Rectangle

def getArea(shape):
    # 方案一
    methods = ('area', 'getArea', 'get_area')
    for method in methods:
        m = getattr(shape, method, None)
        if m:
            return m()
    
    # 方案二:???
    

shape1 = Circle(1)
shape2 = Triangle(2, 3, 4)
shape3 = Rectangle(5, 6)

shapes = [shape1, shape2, shape3]
for _ in map(getArea, shapes):
    print(round(_, 3))
