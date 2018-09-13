#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:10:08 2018

@author: yahkun
"""

'''
实际案例:
    某项目中, 我们从传感器采集数据, 每收集到1G 数据后, 做数据分析, 最终只保存分析结果. 这样
很大的临时数据. 如果常驻内存, 将消耗大量内存资源, 我们可以使用临时文件存储这些临时数据(外部存
储)

临时文件不用命名, 且关闭后会自动被删除.
'''

'''
解决方案:
    使用标准库中tempfile 下的 TemporaryFile, NamedTemporaryFile
'''

from tempfile import TemporaryFile, NamedTemporaryFile

tf = TemporaryFile(buffering=0)
tf.write(b'Hello Python')


ntf = NamedTemporaryFile(delete=False)
ntf.write(b'Hello Python' * 10000)
print(ntf.name)
print(ntf.read())
