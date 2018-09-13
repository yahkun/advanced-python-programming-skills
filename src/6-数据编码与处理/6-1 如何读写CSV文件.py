#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:50:02 2018

@author: yahkun
"""

'''
实际案例:
    http://table.finance.yahoo.com/table.csv?s=000001.sz
    我们可以通过雅虎网站获取中国股市(深市)数据集, 它以 csv 数据格式存储:

Date,Open,High,Low,Close,Volume,Adj Close
2016-06-30,8.69,8.74,8.66,8.70,36220400,8.70
2016-06-29,8.63,8.69,8.62,8.69,36961100,8.69
2016-06-28,8.58,8.64,8.56,8.63,33651900,8.63
......

请将平安银行这只股票, 在2016年中成交量超过30,000,000的记录存储在另一个csv 文件中
'''

'''
解决方案:
    使用标准库中的 csv 模块, 可以使用其中 reader 和 writer 完成 csv 文件读写
'''

import csv

#rf = open('pingan.csv', 'r+')   # py2中应以'rb+'打开文件
#wf = open('pingan_copy.csv', 'a+')  # py2中应以'wb+'打开文件
#csv_reader = csv.reader(rf)
#csv_writer = csv.writer(wf)
#for row in csv_reader:
#    csv_writer.writerow(row)
#
#wf.flush()

with open('pingan.csv', 'r+') as rf:
    csv_reader = csv.reader(rf)
    with open('pingan2.csv', 'w+') as wf:
        csv_writer = csv.writer(wf)
        headers = csv_reader.__next__()
        csv_writer.writerow(headers)
        for row in csv_reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 36000000:
                csv_writer.writerow(row)
print('end')
        