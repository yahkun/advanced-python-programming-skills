#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:25:42 2018

@author: yahkun
"""

'''
实际案例:
    在 web 应用中常用 JSON(JavaScript Object Notation)格式传输数据, 例如我么利用
Baidu语音识别服务做语音识别, 将本地音频数据 post 到 Baidu 语音识别服务器,服务器响应结果为 
json 字符串:
    {
    "corpus_no":"6303355448008565863",
    "err_msg":"success",
    "err_no":0,
    "result":["你好,"],
    "sn":"418359718861467614305"
    }

在 python 中如何读写 json 数据?
'''

'''
解决方案:
    使用标准库中的 json 模块, 其中 loads, dumps 函数可以完成 json 数据的读写.
'''

import json

l = [1, 2, 'abc', {"name": "Bob", "age": 13}]
print(json.dumps(l))    # [1, 2, "abc", {"name": "Bob", "age": 13}]

d = {"a": 123, "b": None, "c": "abc"}
print(json.dumps(d))    # {"a": 123, "b": null, "c": "abc"}

l2 = json.loads(json.dumps(l))
print(l2)

d2 = json.loads(json.dumps(d))
print(d2)

with open('demo.json', 'w') as f:
    json.dump(l, f)
