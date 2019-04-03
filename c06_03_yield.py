#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-04-03 13:24:47
@LastEditTime: 2019-04-03 13:30:41
'''
def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word


print(list(make_word()))
