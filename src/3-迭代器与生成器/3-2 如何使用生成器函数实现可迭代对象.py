#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 16:30:17 2018

@author: yahkun
"""

"""
实际案例:
    实现一个可迭代对象的类, 他能迭代出给定范围内所有素数:
    pn = PrimeNumbers(1, 30)
    for k in pn:
        print(k)
    
    输出结果:
    2 3 5 7 11 13 17 19 23 29
"""

# 解决方案:
# 将该类的 __iter__ 方法实现成生成器函数, 每次 yield 返回一个素数

# 回顾什么是生成器函数
def f():
    print('in f(), 1')
    yield 1
    
    print('in f(), 2')
    yield 2
    
    print('in f(), 3')
    yield 3

g = f() # generator object
print(g.__iter__() is g)


# 实现代码


class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def isPrimeNum(self, k):
        # 该方法效率较低, 只用做解释原理
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True
    
    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(1, 30):
    print(x, end=' ')
    