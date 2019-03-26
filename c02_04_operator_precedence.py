#!/usr/bin/env python
# coding=UTF-8
'''
@Description: operator precedence
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-26 11:18:57
@LastEditTime: 2019-03-26 20:15:21
'''

print(False == False or True)
print(False == (False or True))
print((False == False)or True)

if 1+1 * 3 == 6:
    print("yes")
else:
    print("no")

x = 4
y = 2
if not 1+1 == y or x == 4 and 7 == 8:
    print("yes")
elif x > y:
    print("no")