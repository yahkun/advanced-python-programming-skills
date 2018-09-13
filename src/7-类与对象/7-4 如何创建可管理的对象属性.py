#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 03:57:37 2018

@author: yahkun
"""

'''
实际案例:
    在面向对象编程中, 我们把方法(函数)看做对象的接口. 直接访问对象的属性可能是不安全的, 或设
计上不够灵活. 但是使用调用方法在形式上不如访问属性简洁

circle.getRadius()                 #getter 访问器
circle.setRadius(5.0)  #形式繁琐    #setter 设置器

circle.radius
circle.radius = 5.0    #形式简洁

能否在形式上是属性访问, 但实际上调用方法呢?
'''

'''
解决方案:
    使用 property 函数为类创建可管理对象, fget/fset/fdel 对应相应属性访问
'''

from math import pi

class Circle(object):
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        # 类型检查
        if not isinstance(value, (int, float)):
            raise ValueError('Wrong type.')
        self.__radius = float(value)
    
    def getArea(self):
        return self.radius ** 2 * pi

c = Circle(3.2)

