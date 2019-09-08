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

    def __len__(self):
        return len(self.elements)
    

    def __add__(self, other):
        assert len(self) == len(other)
        sums = []
        for a, b in zip(self.elements, other.elements):
            sums.append(a + b)
        return Vector(*sums)
    
    def __abs__(self):
        c = 0
        for x in self.elements:
            c += x ** 2
        return c ** 0.5
