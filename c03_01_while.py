#!/usr/bin/env python
# coding=UTF-8
'''
@Description: while
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-25 13:03:36
@LastEditTime: 2019-03-27 12:02:48
'''
i = 0
while 1 == 1:
    print(i)
    i += 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")

i = 5
while True:
    print(i)
    i -= 1
    if i <= 2:
        break

i = 0
while True:
    i += 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)
print("Finished")
