#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 05:13:15 2018

@author: yahkun
"""

from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}

print(sorted(d))

#方法1: 使用 zip 函数将字典数据转换成元祖
print(sorted(list(zip(d.values(), d.keys())), reverse=True))

#方法2: 传递 sorted 函数的 key 参数
print(sorted(d.items(), key=lambda x: x[1], reverse=True))
