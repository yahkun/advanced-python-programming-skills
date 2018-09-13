#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:37:52 2018

@author: yahkun
"""

"""
实际案例:
    某软件的log文件,其中的日期格式为'yyyy-mm-dd':
......
2016-05-23 10:59:26 status unpacked python3-pip:all
2016-05-23 10:59:26 status half-configured python3-pip:all
2016-05-23 10:59:26 status installed python3-pip:all
2016-05-23 10:59:26 configure python3-wheel:all 0.24.0-1
......

我们想把其中的日期改为美国日期的格式'mm/dd/yyyy'.
'2016-05-23' => '05/23/2016',应如何处理?
"""

"""
解决方案:
    使用正则表达式 re.sub() 方法做字符串替换, 利用正则表达式的捕获组, 捕获每个部分内容, 在
替换字符串中调整各个捕获组的顺序.
"""

import re

log = open('./sample.log').read()

# 使用位置方式
res1 = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)
# 使用命名方式
res2 = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',
             r'\g<month>/\g<day>/\g<year>',
             log
             )
print(res1)
print(res2)
print(res1 == res2)