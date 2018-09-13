#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:35:04 2018

@author: yahkun
"""

'''
实际案例:
    我么通过雅虎网站获取了中国股市某支股票的 csv 数据文件, 现在要下载多只股票的 csv 文件, 并
    将其转换为 xml/json 文件

如何使用线程来提高下载并处理的效率?
'''

'''
解决方案:
    使用标准库 threading.Thread 创建线程, 在每一个线程中下载并转换一只股票数据
'''