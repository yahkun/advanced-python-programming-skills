#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:28:19 2018

@author: yahkun
"""

"""
实际案例:
某软件要求,从网络上抓取各城市气温信息,并依次显示:
    北京: 15 ~ 20
    天津: 17 ~ 22
    长春: 12 ~ 18
    ...
    
如果一次抓取所有城市天气再显示, 显示第一个城市气温时有很高的延时, 并且浪费存储空间, 我们期望
以"用时访问"的策略, 并且能把所有城市气温封装在一个对象里, 可用for 语句进行迭代. 该如何解决?
"""

##############################################################################
## 1:什么是 iterable 和 iterator ?
#l = [1,2,3,4]
#s = 'abcde'
#for x in l: print(x)
#for x in s: print(x)
#
##由可迭代对象(iterable)得到迭代器对象(iterator)
#
##listiterator
#t = iter(l)     # l.__iter__ 自身迭代器接口
##iterator
#iter(s)     # s.__getitem__ 自身是一个序列
#
## 故: 自身是一个序列 或者 自身具备迭代器接口 的对象是可迭代对象
#
#t.next()    # 1
#t.next()    # 2
#t.next()    # 3
#t.next()    # 4
#t.next()    # StopIteration
#
## 故: for循环的工作原理是: 先使用内置函数 iter() 右可迭代对象得到一个迭代器对象, 再不断的
##调用迭代器对象的 next() 方法, 直到捕获 StopIteration 异常, 循环结束.
##############################################################################

##############################################################################
# 2: 解决方案
# Step 1: 实现一个迭代器对象 WeatherIterator, 调用next方法每次返回一个城市气温
# Step 2: 实现一个可迭代对象 WeatherIterable, 调用__iter__方法返回一个迭代器对象

import requests

#def getWeather(city):
#    r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
#    data = r.json()['data']['forecast'][0]
#    return f"{city}: {data['low']}, {data['high']}"
#
## ['北京', '上海', '广州', '长春']
#print(getWeather('北京'))
#print(getWeather('上海'))

from collections import Iterable, Iterator

#Iterator.__abstractmethods__
#frozenset({'next'})
#Iterable.__abstractmethods__
#frozenset({'__iter__'})

# 实现一个 iterator 对象


class WeatherIterator(Iterator):
    """构造一个天气迭代器的类"""
    
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    
    def getWeather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return f"{city}: {data['low']}, {data['high']}"

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)
    

class WeatherIterable(Iterable):
    """天气可迭代对象"""
    def __init__(self, cities):
        self.cities = cities
        
    def __iter__(self):
        return WeatherIterator(self.cities)
    

for x in WeatherIterable(['北京', '上海', '广州', '长春']):
    print(x)