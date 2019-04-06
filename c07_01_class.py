#!/usr/bin/env python
# coding=UTF-8
'''
@Description: class
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-04-06 10:19:39
@LastEditTime: 2019-04-06 23:47:38
'''


class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
print(felix.color)


class CatMall:
    def __init__(self, cont):
        self.cont = cont


mallweb = CatMall(1)
print(mallweb.cont)
