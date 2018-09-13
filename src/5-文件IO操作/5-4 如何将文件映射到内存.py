#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 20:47:48 2018

@author: yahkun
"""

'''
实际案例:
    1. 在访问某些二进制文件时, 希望能把文件映射到内存中, 可以实现随机访问.(framebuffer设备
文件)
    
    2. 某些嵌入式设备, 寄存器被编址到内存地址空间, 我们可以映射/dev/mem某范围, 去访问这些
寄存器

    3. 如果多个进程映射同一个文件, 还能实现进程间通信的目的
'''

'''
解决方案:
    使用标准库中mmap模块的mmap()函数, 他需要一个打开的文件描述符作为参数.
'''

import mmap

f = open('demo.bin', 'r+b')
#m = mmap.mmap(
#        f.fileno(), 
#        0, 
#        access=mmap.ACCESS_WRITE
#        )
#print(m)        # <mmap.mmap object at 0x11119afa8>
## 可以像列表一样支持索引和切片  
#print(m[0])     # 0(py3) '\x00'(py2)
#print(m[10:20]) # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'(py3)
#                # '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'(py2)
## 修改文件内容, 
#m[15] = 15
#
#print(m[10:20])
## dd if=/dev/zero of=demo.bin bs=1024 count=1024
## shell 中使用 od -x demo.bin 查看内容

# mmap.PAGESIZE 以内存页的整数倍进行映射
m = mmap.mmap(
        f.fileno(), 
        mmap.PAGESIZE * 8, 
        access=mmap.ACCESS_WRITE, 
        offset=mmap.PAGESIZE * 4
        )
m[:100] = b'\3' * 100
print(m[:100])
