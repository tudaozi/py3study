#!/usr/bin/env python
# coding=UTF-8
'''
@Description:
@Author: Tudaozi
@WebSite: https://www.staurl.com
@LastEditors: Tudaozi
@Date: 2019-04-08 09:39:19
@LastEditTime: 2019-04-08 10:20:14
'''


class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
'''
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
