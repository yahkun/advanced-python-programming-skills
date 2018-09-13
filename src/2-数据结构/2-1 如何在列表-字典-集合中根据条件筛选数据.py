#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 01:43:07 2018

@author: yahkun
"""

from random import randint

###########################################################################

#############
## 列表解析 ##
############

## 随机生成一个列表
#data = [randint(-10, 10) for x in range(10)]
#print(len([x for x in data if x < 0]))
#
## 方法一: for loop + if
#def list_filter_1(data_list):
#    res = []
#    for x in data_list:
#        if x >= 0:
#            res.append(x)
#    #print(f'方法一的输出为{res}')
#
#
## 方法二: builtin_function_or_method: filter()
#def list_filter_2(data_list):
#    filter(lambda x: x >= 0, data)
#    #print(f'方法二的输出为{res}')
#
#
## 方法三: 列表解析式
#def list_filter_3(data_list):
#    [x for x in data if x >= 0]
#    #print(f'方法三的输出为{res}')
#
#
## 比较三种方式的性能优劣
## list_filter_2 优于 list_filter_3 优于 list_filter_1
#import timeit
#t1 = timeit.Timer(lambda: list_filter_1(data)).timeit(1)
#t2 = timeit.Timer(lambda: list_filter_2(data)).timeit(1)
#t3 = timeit.Timer(lambda: list_filter_3(data)).timeit(1)

##########################################################################

#############
## 字典解析 ##
############

## 随机生成一个字典
#d = {x: randint(60, 100) for x in range(1, 21)}
#
#print({k: v for k, v in d.items() if v > 90})

##########################################################################

#############
## 集合解析 ##
############

#s = {randint(-10, 10) for x in range(10)}
#print({x for x in s if x % 3 == 0})