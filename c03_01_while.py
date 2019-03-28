#!/usr/bin/env python
# coding=UTF-8
'''
@Description: while
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-25 13:03:36
@LastEditTime: 2019-03-28 13:33:38
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

age = 15
while age > 1:
    age -= 1
    if age == 12:
        continue
    print(age)
print("end")
