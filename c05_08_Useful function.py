#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-29 14:19:07
@LastEditTime: 2019-03-29 18:08:19
'''
print(", ".join(["spam", "eggs", "ham"]))
# 打印 "spam, eggs, ham"
#使用其他字符串作为分隔符连接字符串列表

print("|".join(["span","eggs","ham"]))
print(" and ".join(["span","eggs","ham"]))

#replace - 使用其他字符串替换字符串中的一个子字符串
print("Hello ME".replace("ME", "world"))
# 打印 "Hello world"
print("Your My".replace("My","Name"))

startswith 和 endswith - 确定是否在字符串的开始和结尾处有一个子字符串。
print("This is a sentence.".startswith("This"))
# 打印 "True"

print("This is a sentence.".endswith("sentence."))
# 打印 "True"

print("This is a sentence.".upper())
# 打印 "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
# 打印  "an all caps sentence"

print("spam, eggs, ham".split(", "))
# 打印  "['spam', 'eggs', 'ham']"
