#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 19:32:54 2018

@author: yahkun
"""

"""
实际案例:
    有某个文本文件, 我们想读取其中某范围的内容如100~300行之间的内容, Python中文本文件是
可迭代对象, 我们能否可以使用类似列表切片的方式得到一个100~300行文件内容的生成器?

f = open('/var/log/dmesg')
f[100:300]    #可以吗?
"""

"""
解决方案:
    使用标准库中的 itertools.islice 它能返回一个迭代对象切片的生成器
"""

from itertools import islice

f = open('./alice.txt')

# 可能导致内存不足,浪费内存空间
#lines = f.readlines()
#print(lines[100:300])

islice(f, 100, 300)
for line in islice(f, 100, 300):
    print(line)
    
# islice(f, 500) 前500行
# islice(f, 100, none) 100行至文件末尾


## 这里需注意!!!
l = [x for x in range(20)]
t = iter(l)
for x in islice(t, 5, 10):
    print(x)

for x in t:
    print(x)
    