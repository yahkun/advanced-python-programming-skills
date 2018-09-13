#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 19:58:56 2018

@author: yahkun
"""

"""
实际案例:
    我们要把某个字符串依据分隔符拆分成不同的字段, 该字符串包含多种不同的分隔符, 例如:
    
s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

其中<,>, <;>, <|>, <\>都是分隔符, 如何处理?
"""

"""
解决方案:
    方案一: 连续使用 str.split()方法, 每次处理一种分割符号
    方案二【推荐】: 使用正则表达式的 re.split()方法, 一次性拆分字符串
"""

s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

# 方案一
#def mySplit(s, ds):
#    res = [s]
#    
#    for d in ds:
#        t = []
#        map(lambda x: t.extend(x.split(d)),res)
#        res = t
#    return [x for x in res if x]
#
#print(mySplit(s, ';,|\t'))

# 方案二
import re

res = re.split(r'[,;\t|]+', s)
print(res)