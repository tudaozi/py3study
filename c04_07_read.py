#!/usr/bin/env python
# coding=UTF-8
'''
@Description: read
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-28 15:17:12
@LastEditTime: 2019-03-28 16:04:16
'''
file1 = open("C:/Users/lzp/Code/Repository/py3study/filename1.txt", "r")
cont = file1.read()
print(cont)
file1.close()


file2 = open("C:/Users/lzp/Code/Repository/py3study/filename1.txt", "r")
print(file2.read(3))
print(file2.read(4))
print(file2.read(4))
print(file2.read())
file2.close()

file3 = open("C:/Users/lzp/Code/Repository/py3study/filename1.txt", "r")
print(file3.readlines())
file3.close()

file4 = open("C:/Users/lzp/Code/Repository/py3study/filename1.txt", "r")
for line in file4:
    print(line)
file4.close()
