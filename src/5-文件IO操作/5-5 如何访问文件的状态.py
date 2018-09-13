#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:40:01 2018

@author: yahkun
"""

'''
实际案例:
    在某些项目中, 我们需要获得文件状态, 例如:
        1. 文件的类型(普通文件, 目录, 符号链接, 设备文件...)
        2. 文件的访问权限
        3. 文件的最后访问/修改/节点状态更改时间
        4. 普通文件的大小
        ......
'''

'''
解决方案:
    方案一: 系统调用
        标准库 os模块下的三个系统调用stat, fstat, lstat获取文件状态
    方案二【推荐】: 快捷函数
        标准库中 os.path 下一些函数, 使用起来更加简洁
'''

import os, stat, time

# 方案一
# 使用 os.py 模块中的API获取:
            # os.stat().st_mode  
            # os.stat().st_atime; os.stat().st_mtime; os.stat().st_ctime
            # os.stat().st_size
s = os.stat('a.txt')    
smode = s.st_mode
stimes = [s.st_atime, s.st_mtime, s.st_ctime]
ssize = s.st_size

## 1. 文件的类型(普通文件, 目录, 符号链接, 设备文件...)
## 使用 stat.py 模块中的API访问文件的状态
#dir_is = stat.S_ISDIR(smode)
#print(dir_is)
#reg_is = stat.S_ISREG(smode)
#print(reg_is)
#
## 2. 文件的访问权限
#usr_read_competence = smode & stat.S_IRUSR > 0
#print(f'当前用户可读权限: {usr_read_competence}')  
#usr_write_competence = smode & stat.S_IWUSR > 0
#print(f'当前用户可写权限: {usr_write_competence}')
#usr_exec_competence = smode & stat.S_IXUSR > 0
#print(f'当前用户可执行权限: {usr_exec_competence}')
#grp_read_competence = smode & stat.S_IRGRP > 0
#print(f'组用户可读权限: {grp_read_competence}')
#oth_read_competence = smode & stat.S_IROTH > 0
#print(f'其他用户可读权限: {oth_read_competence}')
#
## 3. 文件的最后访问/修改/节点状态更改时间
#def convert_datetime(month, day, year, hour, minute, second):
#    """以人类的习惯打印时间格式"""
#    
#    dt = f'{month}/{day}/{year} {hour}:{minute}:{second}'
#    return dt
#
#def print_msg(string, dt):
#    """
#    完整打印日期时间信息
#    文件的最后访问时间是: 3/8/2018 15:55:57
#    """
#    print(f'文件的最后{string}时间是: {dt}')
#
#stimes = [time.localtime(stime) for stime in stimes]
#
#l = ['访问', '修改', '节点状态更改']
#n = 0
#for stime in stimes:
#    dt = convert_datetime(
#                        stime.tm_mon,
#                        stime.tm_mday,
#                        stime.tm_year,
#                        stime.tm_hour,
#                        stime.tm_min,
#                        stime.tm_sec
#                        )
#    print_msg(l[n], dt)
#    n += 1
#
## 4. 普通文件的大小
#os.stat('a.txt').st_size

# 方案二
## 1. 文件的类型(普通文件, 目录, 符号链接, 设备文件...)
os.path.isdir('a.txt') #直接返回 bool 值
os.path.isfile('a.txt')

## 2. 文件的访问权限（没有接口，使用第一种方法）

## 3. 文件的最后访问/修改/节点状态更改时间
os.path.getatime('a.txt')
os.path.getmtime('a.txt')
os.path.getctime('a.txt')

## 4. 普通文件的大小
os.path.getsize('a.txt')