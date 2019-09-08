# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:12:34 2019

@author: s120264
"""

class Vector:
    def __init__(self, *elements):
        self.elements = elements

    def __repr__(self):
        s = '['
        for x in self.elements:
            s += str(x) + ', '
        s += ']'
        return s
