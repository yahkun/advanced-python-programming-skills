#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:38:40 2018

@author: yahkun
"""

'''
实际案例:
    由于全局解释器锁的存在, 多线程进行 CPU 密集型操作并不能提高执行效率, 我们修改程序架构:
        1. 使用多个 DownloadThread 线程进行下载(I/O操作)
        2. 使用一个 ConvertTread 线程进行转换(CPU 密集型操作)
        3. 下载线程把下载数据安全地传递给转换线程
'''