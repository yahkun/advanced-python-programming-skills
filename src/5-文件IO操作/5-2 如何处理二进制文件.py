#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:08:25 2018

@author: yahkun
"""

"""
实际案例:
    wav 是一种音频文件格式, 音频文件为二进制文件. wav 文件由头部信息和音频采样数据构成.
前44个字节为头部信息, 包括声道数, 采样频率, PCM位宽等等, 后面是音频采样数据.

使用 Python, 分析一个 wav 文件头部信息, 处理音频数据.
"""

"""
解决方案:
    open 函数指定mode参数为'b'以二进制模式打开文件;
    二进制数据可以用readinto, 读入到提前分配好的buffer中, 便于数据处理;
    解析二进制数据可以使用标准库中的struct模块的unpack方法.
"""