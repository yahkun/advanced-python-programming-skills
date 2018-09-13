#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:06:15 2018

@author: yahkun
"""

# lib1.py
class Circle(object):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return self.r ** 2 * 3.14
