#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-25 13:03:36
@LastEditTime: 2019-03-26 22:41:55
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
