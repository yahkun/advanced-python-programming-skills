#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 05:32:49 2018

@author: yahkun
"""

from random import randint, sample

# 每个字母代表一个球员
data = sample('abcdefg', randint(3, 6))

s1 = {x: randint(1, 4) for x in data}
s2 = {x: randint(1, 4) for x in data}
s3 = {x: randint(1, 4) for x in data}

#方法1
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print(res)
        
#方法2: 使用集合(set)的交集操作
#   Step1: 使用字典的 viewkeys() 方法, 得到一个字典keys 的集合
#   Step2: 使用 map 函数,得到所有字典的keys的集合
#   Step3: 使用 reduce 函数,取所有字典的 keys 的集合的交集

# s1.keys() & s2.keys() & s3.keys() #原理

from functools import reduce
res = reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3]))
print(res)