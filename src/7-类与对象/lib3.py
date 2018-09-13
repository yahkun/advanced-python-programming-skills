#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:30:28 2018

@author: yahkun
"""

# lib3.py
class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        
    def get_area(self):
        return self.w * self.h
    