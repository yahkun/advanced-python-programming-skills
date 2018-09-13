#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 00:49:26 2018

@author: yahkun
"""

'''
实际案例:
    某些时候, 我们需要将其他格式数据转换为 xml, 例如, 我们要把平安股票 csv 文件, 转换成相应
的 xml 文件.

pingan.csv
Date,Open,High,Low,Close,Volume,Adj Close
2016-06-30,8.69,8.74,8.66,8.70,36220400,8.70
pingan.xml
<Data>
    <Row>
        <Date>2016-07-05</Date>
        <Open>8.80</Open>
        <High>8.83</High>
        <Low>8.77</Low>
        <Close>8.81</Close>
        <Volume>42203700</Volume>
        <AdjClose>8.81</AdjClose>
    </Row>
</Data>
'''

'''
解决方案:
    使用标准库中的 xml.etree.ElementTree, 构建 ElementTree, 使用 write 方法写入文件
'''

import csv
from xml.etree.ElementTree import Element, ElementTree

def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

def csvToxml(fname):
    with open(fname, 'r+') as f:
        csv_reader = csv.reader(f)
        headers = csv_reader.__next__()
        
        root = Element("Data")
        for row in csv_reader:
            eRow = Element("Row")
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)

    pretty(root)
    return ElementTree(root)



et = csvToxml('pingan.csv')
et.write('pingan.xml')