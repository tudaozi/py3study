#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-04-05 23:22:29
@LastEditTime: 2019-04-06 00:03:17
'''
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])
print(num_set)
print(word_set)


print(3 in num_set)
print("spam" not in word_set)

space = set()
space1 = {}

print(space)
print(space1)

letters = {"a", "b", "c", "d"}
if "f" not in letters:
    print(1)
else:
    print(2)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
print(type(nums))

nums.add(-7)
nums.remove(3)
print(nums)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)
print(first & second)
print(first-second)
print(second-first)
print(first ^ second)
