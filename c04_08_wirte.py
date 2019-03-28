#!/usr/bin/env python
# coding=UTF-8
'''
@Description: write
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-03-28 16:03:57
@LastEditTime: 2019-03-28 18:22:41
'''
file1 = open("C:/Users/lzp/Code/Repository/py3study/filename2.txt", "w")
file1.write("This has been written to a file")
file1.close()

file2 = open("C:/Users/lzp/Code/Repository/py3study/filename4.txt", "w")
file2.write("This has been written to a file")
file2.close()

file3 = open("C:/Users/lzp/Code/Repository/py3study/filename4.txt", "r")
print("Reading initial contents")
print(file3.read())
print("Finished")
file3.close()

file4 = open("C:/Users/lzp/Code/Repository/py3study/filename5.txt", "w")
file4.write("Some new text")
file4.close()

file5 = open("C:/Users/lzp/Code/Repository/py3study/filename5.txt", "r")
print("Reading new contents")
print(file5.read())
print("Finished")
file5.close()

file6 = open("C:/Users/lzp/Code/Repository/py3study/filename5.txt", "w")
file6.close()


msg="Hello World!"
file7=open("")