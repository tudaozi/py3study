#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-28 16:03:57
@LastEditTime: 2019-03-28 16:10:24
'''
file1 = open("C:/Users/lzp/Code/Repository/py3study/filename2.txt", "w")
file1.write("This has been written to a file")
file1.close()

file2 = open("C:/Users/lzp/Code/Repository/py3study/filename4.txt", "w")
file2.write("This has been written to a file")
file2.close()

file3=open("C:/Users/lzp/Code/Repository/py3study/filename4.txt","r")
print("Reading initial contents")
print(file3.read())
print("Finished")
file3.close()