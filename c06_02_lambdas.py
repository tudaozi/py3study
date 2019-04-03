#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-04-03 12:11:34
@LastEditTime: 2019-04-03 13:23:44
'''
def my_func(f, arg):
    return f(arg)


my_func(lambda x: 2*x*x, 5)


def polynomial(x):
    return x**2+5*x+4


print(polynomial(-4))


print((lambda x: x**2+5*x+4)(-4))
