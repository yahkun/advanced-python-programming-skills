#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 02:08:30 2018

@author: yahkun
"""

'''
实际案例:
    Microsoft Excell是日常办公中使用最频繁的软件, 其数据格式为 xls, xlsx, 一种非常常用的
电子表格.
    小学某班级成绩, 记录在 excel 文件中:

姓名    语文    数学    外语
李雷    95      99     96
韩梅梅   98      100    93
...

利用 Python 读写 excel, 添加"总分"列, 计算每人总分.
'''

'''
解决方案:
    使用 pip 安装 #pip install xlrd xlwt
    使用第三方库 xlrd 和 xlwt, 这两个库分别用于 excel 读和写
'''

import xlrd, xlwt

# 读取 excel 文件
rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, '总分', None)

for row in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(row, 1))
    rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)

# 写入 excel 文件
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)

style = xlwt.easyxf('align: vertical center, horizontal center')

for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r, c, rsheet.cell_value(r, c), style)

wbook.save('output.xlsx')