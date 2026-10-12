#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:08:19 2026

@author: gecpi
"""

class shape:
    def getArea(self):
        print("area of shape is undefined" )
    def getperimeter(self):
        print("perimeter of the shape is undefined")
# child class
class Triangle(shape):
    def __init__(self,base,height):
        self.b,self.h=base,height
    def getDim(self):
        print
    def getArea(self):
        area=0.5*self.b*self.h
        return area
    def getperimeter(self):
        return super().getperimeter()
s.Triangle(5,8)
T.getDim()
print(f"Area(Tri)-{T.getperimeter()}")
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.l,self.b=length,breadth
    def getDim(self):
        print
    def getArea(self):
        area=self.l*self.b
        return area
    def getperimeter(self):
        return super().getperimeter()
    