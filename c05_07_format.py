#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-29 14:01:32
@LastEditTime: 2019-03-29 14:17:28
'''
# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)


print("{0}{1}{0}".format("abra", "cad"))

print("{2}{1}{0}".format("abc", "bcd", "def"))

a = "{x}, {y}".format(x=5, y=12)
print(a)

str = "{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)
