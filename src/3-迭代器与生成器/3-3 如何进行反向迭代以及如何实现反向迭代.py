#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 16:48:11 2018

@author: yahkun
"""

"""
实际案例:
    实现一个连续浮点数发生器 FloatRange (和range类似), 根据给定范围(start, end)和步进值
(step)产生一系列连续浮点数, 如迭代 FloatRange(3.0, 4.0, 0.2) 可产生序列:
    正向: 3.0 -> 3.2 -> 3.4 -> 3.6 -> 3.8 -> 4.0
    反向: 4.0 -> 3.8 -> 3.6 -> 3.4 -> 3.2 -> 3.0
"""

# 对序列 l 执行反向迭代操作
l = [x for x in range(1, 6)]

# l.reverse()改变了原序列, 在某种情况下不允许这种操作
# l[::-1] 这种方式会得到和原序列同样的长度,浪费内存空间
# 推荐下面这种方式: iter(l), reversed(l)
#iter(l)     #得到一个 listiterator 列表迭代器 = l.__iter__()
#reversed(l) #得到一个 listreverseiterator 列表反向迭代器 = l.__reversed__()
#for x in reversed(l):
#    print(x)

"""
解决方案:
    实现反向迭代协议的__reversed__方法, 它返回一个反向迭代器
"""


class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step
    
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(x)