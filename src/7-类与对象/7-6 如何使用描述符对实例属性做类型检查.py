#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 05:01:35 2018

@author: yahkun
"""

'''
实际案例:
    在某项目中, 我们实现了一些类, 并希望能像静态类型语言那样(C, C++, Java)对他们的实例属性
做类型检查.

p = Person()
p.name = 'Bob'  #必须是 str
p.age = 18      #必须是 int
p.height = 1.83 #必须是 float

要求:
    1.可以对实例变量名指定类型
    2.赋予不正确类型时抛出异常
'''

'''
解决方案:
    使用描述符实现需要类型检查的属性:
        分别实现__get__, __set__, __delete__方法, 在__set__内使用 isinstance 函数做
类型检查
'''
## 讲解
#class Descriptor(object):
#    def __get__(self, instance, cls):
#        print('in __get__', instance, cls)
#        # return instance.__dict__[xxx]
#    
#    def __set__(self, instance, value):
#        print('in __ set')
#        # instance.__dict__[xxx] = value
#    
#    def __delete__(self, instance):
#        print('in __del__')
#        # del instance.__dict__[xxx]
#
#class C(object):
#    d = Descriptor()
#
#c = C()
#c.d


# 例子
class Attr(object):
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __get__(self, instance, cls):
        print('in __get__', instance, cls)
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        print('in __ set')
        if not isinstance(value, self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        print('in __del__')
        del instance.__dict__[self.name]


class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)

p = Person()
p.name = 'Bob'
print(p.name)

