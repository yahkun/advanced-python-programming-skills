#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:25:32 2018

@author: yahkun
"""

"""
实际案例:
    某文本文件编码格式已知(如UTF-8, GBK, BIG5), 在Python 2.x和Python 3.x 中分别如何
读取该文件?
"""

"""
解决方案:
    字符串的语义发生了变化:
    Python2          Python3
    ------------------------
    str        ->    bytes
    unicode    ->    str

Python 2.x写入文件前对 unicode 编码, 读入文件后对二进制字符串解码.
Python 3.x open函数指定't'的文本格式, endcoding 指定编码格式.

注: 文本永远以字节串(bytes)形式存储; 以字符串(str)形式显示
"""

## Python 2.x 手动编解码
#
## 写入文本
#f = open('py2.txt', 'w')
#s = u'你好'
#f.write(s.encode('gbk'))
#f.close()
## 读取文本
#f = open('py2.txt', 'r')
#t = f.read()
#print(t)
#s = t.decode('gbk')
#print(s)
#f.close()

# Python 3.x 自动编解码

# 写入文本
f = open('py3.txt', 'wt', encoding='utf8')
s = '你好, 我爱编程!'
f.write(s)
f.close()
# 读取文本
f = open('py3.txt', 'rt', encoding='utf8')
s = f.read()
print(s)
f.close()