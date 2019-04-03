#!/usr/bin/env python
# coding=UTF-8
'''
@Description: functional programming
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-31 00:26:20
@LastEditTime: 2019-04-03 22:02:41
'''


def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


print(apply_twice(add_five, 10))


def fp_one(fp, arg1, arg2):
    return fp(fp(arg1, arg2), arg1)


def fp_two(x, y):
    return x+y


print(fp_one(fp_two, 20, 30))


def fp_three(fp_four, fp_five, arg1, arg2, arg3, arg4, arg5):
    return fp_four(arg1, arg2)+fp_five(fp_four(arg1, arg2), arg3, arg4)


def fp_four(x, y):
    return x*y


def fp_five(a, b, c):
    return (a+b) % c


print(fp_three(fp_four, fp_five, 1, 2, 3, 4, 100))


print(3/2)
print(3//2)
print(5 % 2)
