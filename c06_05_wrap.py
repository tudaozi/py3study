#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-04-03 22:16:06
@LastEditTime: 2019-04-04 00:32:02
'''


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


def print_text():
    print("Hello world!")


decorated = decor(print_text)
decorated()


def my_sum(x, y):
    """
    result is the sum of x and y
    """

    print(x+y)


def func_decor(func):
    def new_func_decor(arg1, arg2):
        print("The func name is: ", func.__name__)
        print("The func doc is: ", func.__doc__)
        print("=================")
        func(arg1, arg2)
        print("=================")
    return new_func_decor


func_decor1 = func_decor(my_sum)
func_decor1(3, 4)


def my_sums(a, b, c, d):
    print((a+b-c)/d)


def sums_decor(func):
    def new_sums_decor(arg1, arg2, arg3, arg4):
        print("=====================")
        func(arg1, arg2, arg3, arg4)
        print("=====================")
    return new_sums_decor


sums_decor1 = sums_decor(my_sums)
sums_decor1(1, 2, 3, 4)
