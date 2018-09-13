#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 04:34:30 2018

@author: yahkun
"""
from random import randint
from collections import Counter


#实际案例:
# 1. 某随机序列中, 找到出现次数最高的三个元素, 他们出现的次数是多少?
# 2. 对某英文文章的单词进行词频统计, 找到出现次数最高的10个单词, 他们出现的次数是多少?


# 生成一个随机序列
data = [randint(0, 20) for _ in range(30)]


##方法1
#c = dict.fromkeys(data, 0)
#for x in data:
#    c[x] += 1
#print(c)
#res = sorted(c.items(), key=lambda d:d[1], reverse=True)[:3]
#print(res)


##方法2
#   使用 collections.Counter 对象,将序列传入 Counter 的构造器,得到 Counter 对象是元素
#频度的字典
#   Counter.most_common(n)方法得到频度最高的 n个元素的列表

#c2 = Counter(data)
#print(c2)
#print(c2.most_common(3))

#import re
#txt = open('CodingStyle').read()
#c3 = Counter(re.split('\W+', txt))
#c3.most_common(10)
