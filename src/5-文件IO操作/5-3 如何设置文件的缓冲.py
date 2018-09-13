#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:28:21 2018

@author: yahkun
"""

"""
实际案例:
    将文件内容写入到硬件设备时(以字节块block的单位写入), 使用系统调用, 这类 I/O 操作非常耗时, 
为了减少 I/O 操作的次数, 文件通常使用缓冲区.(有足够多的数据才进行系统调用)文件的缓冲行为, 
分为全缓冲, 行缓冲(tty终端设备), 无缓冲(串口设备).

如何设置Python中文件对象的缓冲行为?
"""

## Python中文件I/O操作默认的缓冲行为
#
#f = open('demo.txt', 'w')
#f.write('abc')      # 'abc'进入到缓冲区等待写入
#f.write('+' * 4093) # 4093个'+'进入到缓冲区等待写入
#f.write('-')        # 将上一个块block写入文件中, '-'进入缓冲区等待写入
#f.write('*' * 4095) # 4095个'*'进入到缓冲区等待写入
#f.write('#')        # 将上一个块block写入文件中, '#'进入缓冲区等待写入
#f.close()

"""
解决方案:
    全缓冲: open函数的buffering设置为大于1的整数n，n为缓冲区大小。
    行缓冲：open函数的buffering设置为1
    无缓冲：open函数的buffering设置为0
"""

## 全缓冲
#f = open('demo2.txt', 'w', buffering=2048)
#f.write('abc')
#f.write('=' * 2045)
#f.write('xyz')
#f.close()

## 行缓冲 (only usable in text mode with Python3.x)
#f = open('demo3.txt', 'w', buffering=1)
#f.write('abc')
#f.write('123')
#f.write('\n')
#f.write('xyz\n')
#f.close()

# 无缓冲 (only allowed in binary mode with Python3.x)
f = open('demo4.txt', 'wb', buffering=0)
f.write(b'a')
f.write(b'b')
f.write(b'c')
f.close()