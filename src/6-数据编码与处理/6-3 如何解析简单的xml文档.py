#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:35:42 2018

@author: yahkun
"""

'''
实际案例:
    xml 是一种十分常用的标记性语言, 可提供统一的方法来描述应用程序的结构化数据:

Python 中如何解析 xml 文档?
'''

'''
解决方案:
    使用标准库中的 xml.etree.ElementTree, 其中的 parse 函数可以解析 xml 文档
'''

from xml.etree.ElementTree import parse

f = open('demo.xml')
et = parse(f)
root = et.getroot()

# 获取子元素

# 1
for child in root:
    print(child.get('name'))

# 2
for child in root.getchildren():
    print(child.get('name'))

"""
res1 = []

res2 = []

for child in root:
    res1.append(child)

for child in root.getchildren():
    res2.append(child)

res1
Out[59]: 
[<Element 'country' at 0x114b33548>,
 <Element 'country' at 0x114b239f8>,
 <Element 'country' at 0x114b43c78>]

res2
Out[60]: 
[<Element 'country' at 0x114b33548>,
 <Element 'country' at 0x114b239f8>,
 <Element 'country' at 0x114b43c78>]

res1 == res2
Out[61]: True

res1 is res2
Out[62]: False
"""

# 3 
children = root.findall('country')
for child in children:
    print(child.get('name'))

# 4
children = root.iterfind('country')
for child in children:
    print(child.get('name'))
    
# 5
print(list(root.iter()))
print(list(root.iter('rank')))