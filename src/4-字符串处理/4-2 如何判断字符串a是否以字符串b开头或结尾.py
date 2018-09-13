#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:35:43 2018

@author: yahkun
"""

"""
实际案例:
    某文件系统目录下有一系列文件:
    quicksort.c
    graph.py
    heap.java
    install.sh
    stack.cpp
    ...
编写程序给其中所有的.sh文件和.py文件加上用户可执行权限
"""

"""
解决方案:
    使用字符串的 str.startswith() 和 str.endswith() 方法.
    注意:多个匹配时, 参数应使用元祖.
"""

import os, stat

names = os.listdir('./sample')
t_names = [name for name in names if name.endswith(('.sh', '.py'))]

for name in t_names:
    os.chmod(
            f'./sample/{name}', 
            os.stat(f'./sample/{name}').st_mode | stat.S_IXUSR
    )