#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:22:35 2018

@author: yahkun
"""

"""
实际案例:
    1.过滤掉用户输入中前后多余的空白字符:
'  nick2008@gmail.com  '
    2.过滤某 windows 下编辑文本中的'\r':
'hello world\r\n'
    3.去掉文本中的 unicode 组合符号(例如音调等):
u'ní hǎo, chí fàn'
"""

"""
解决方案:
    方案一:字符串 strip(), lstrip(), rstrip() 方法去掉字符串两端字符.
    方案二:删除单个固定位置的字符, 可以使用切片+拼接的方式.
    方案三:字符串的 replace() 方法或正则表达式 re.sub() 删除任意位置字符.
    方案四:字符串的 translate() 方法, 可以同时删除多种不同字符.
"""

import re

## 方案一:【推荐使用】
#s1 = '   abc   123   '
#print('|' + s1 + '|')
#print('|' + s1.strip() + '|')
#print('|' + s1.lstrip() + '|')
#print('|' + s1.rstrip() + '|')
#
#s1 = '++-abc-+-123--+'
#print(s1)
#print(s1.strip('+-'))
#print(s1.lstrip('+-'))
#print(s1.rstrip('+-'))
#
## 方案二:
#s2 = 'abc:123'
#print(s2)
#s2 = s2[:3] + '' + s2[4:]
#print(s2)
#
## 方案三: 【推荐使用】
#s3 = '\tabc\t123\txyz'
#print(s3)
#s3 = s3.replace('\t', '')
#print(s3)
#
#s3 = '\tabc\t123\txyz\r456\r'
#print(s3)
#s3 = re.sub('[\t\r]', '', s3)
#print(s3)

# 方案四: Python3中已不推荐使用!!! 
s4 = 'abc123xyz'
print(s4)
s4 = s4.translate(str.maketrans('abcxyz', 'xyzabc'))    
# Python2 => string.maketrans()
print(s4)

s4 = '\tabc\r123\nxyz'
print(s4)
#s4 = s4.translate({ord('\t'):None, ord('\r'):None, ord('\n'):None})
s4 = s4.translate(dict.fromkeys([ord('\t'), ord('\r'), ord('\n')]))
print(s4)
