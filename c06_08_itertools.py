#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-04-06 00:22:08
@LastEditTime: 2019-04-06 10:18:53
'''
from itertools import count, cycle, repeat, accumulate, takewhile, product

for i in count(3):
    print(i)
    if i >= 11:
        break
count1 = 0
for item in cycle("x"):
    if count1 >= 7:
        break
    print(item)
    count1 += 1

nums_list = list(range(10))
print(nums_list)
nums = list(accumulate(range(10)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

a = {1, 2}
print(len(list(product(range(3), a))))


print(list(range(3)))
print(list({1, 2}))
