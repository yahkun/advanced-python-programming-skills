#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:55:38 2018

@author: yahkun
"""

"""
实际案例:
    某个字典存储了一系列属性值,
{
     "lodDist": 100.0,
     "SmallCull": 0.04,
     "DistCull": 500.0,
     "trilinear": 40,
     "farclip": 477
}

在程序中, 我们想以以下工整的格式将其内容输出, 如何处理?
SmallCull : 0.04
farclip   : 477
lodDist   : 100.0
DistCull  : 500.0
trilinear : 40
"""

"""
解决方案:
    方案一:使用字符串的 str.ljust() str.rjust() str.center() 进行左, 右, 居中对齐.
    方案二:使用 format() 方法, 传递类似 '<20', '>20', '^20' 参数完成同样的任务.
"""

## 演示
#s = 'abc'
#
#print('左对齐')
#print(s.ljust(20, '*'))
#print(format(s, '<20'))
#print('右对齐')
#print(s.rjust(20, '*'))
#print(format(s, '>20'))
#print('居中对齐')
#print(s.center(20, '*'))
#print(format(s, '^20'))

d = {
     "lodDist": 100.0,
     "SmallCull": 0.04,
     "DistCull": 500.0,
     "trilinear": 40,
     "farclip": 477
}
largest_width = max(map(len, d.keys()))
for k in d:
    print(k.ljust(largest_width), ':', d[k])