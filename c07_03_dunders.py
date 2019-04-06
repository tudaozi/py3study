#!/usr/bin/env python
# coding=UTF-8
import random
'''
@Description: class
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-04-06 22:19:44
@LastEditTime: 2019-04-07 01:25:43
'''


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("spam")
print(spam.cont)
hello = SpecialString("Hello world!")
print(hello.cont)
print(spam / hello)


class Specialstring:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


spam = Specialstring("spam")
eggs = Specialstring("eggs")
spam > eggs


print(list(range(5)))
print(len("eggs"))

eg = "eggs"
print(eg[2])


class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)


vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

vague_list1 = ["A", "B", "C", "D", "E"]
print(vague_list1[2])
