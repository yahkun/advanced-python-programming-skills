#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 03:22:19 2018

@author: yahkun
"""

'''
实际案例:
    我们实现了一个 telnet 客户端的类 TelnetClinet, 调用实例的 start()方法启动客户端与服
务器交互, 交互完毕后需调用 cleanup()方法, 关闭已连接的 socket, 以及将操作历史纪录写入文件
并关闭.

能否让 TelnetClient 的实例支持上下文管理协议, 从而替代手工调用 cleanup()方法
'''

'''
解决方案:
    实现上下文管理协议, 需要定义实例的__enter__, __exit__方法, 他们分别在 with 开始和结束时被
调用
'''

#with open('demo.txt', 'w+') as f:
#    f.write('Hello Python!\n')
#    f.writelines(['Life is short, ', 'I use Python!\n'])
##f.close()
    
from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque

class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None
    
    def start(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        
        # user
        t = self.tn.read_until('Login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)
        
        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]):
            t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())
        
        # 进入 shell 交互
        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('s ')
            stdout.write(t[len(uinput) + 1:])
        
    def cleanup(self):
        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt', 'w+') as f:
            f.writelines(self.history)

client = TelnetClient('127.0.0.1')
print('\nStart...')
client.start()
print('\nCleanup...')
client.cleanup()
