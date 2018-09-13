#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 04:10:01 2018

@author: yahkun
"""

# 程序中大量索引会降低程序可读性, 该如何解决这个问题?

# 解决方案
    # 方案一: 定义类似与其他语言的枚举类型, 也就是定义一系列数字常量
    # 方案二: 使用标准库中 collections.namedtuple 替代内置 tuple
    
# ('Jim', 16, 'male', 'jim8721@gmail.com')
# ('LiLei', 17, 'male', 'leili@qq.com')
# ('Lucy', 16, 'female', 'lucy123@yahoo.com')

# 方案一
#NAME, AGE, GENDER, EMAIL = range(4)
#
#student = ('Jim', 16, 'male', 'jim8721@gmail.com')
#
## name
#print(student[NAME])
#
## age
#if student[AGE] >= 18:
#    pass
#
## gender
#if student[GENDER] == 'male':
#    pass

# 方案二
from collections import namedtuple

student = namedtuple('student', ['name', 'age', 'gender', 'email'])
s = student('Jim', 16, 'male', 'jim8721@gmail.com')
print(s)

# name
print(s.name)

# age
print(s.age)

# gender
print(s.gender)