# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         链表
# Author:       Nino
# Date:         2020/10/23
# Note:         单向链表
# -------------------------------------------------------------------------------
class Node:
    def __init__(self, value = None, next = None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, value):
        self._value = value

    def setNext(self, next):
        self._next = next

class Linkedlist:
    def __init__(self):
        self._head = None
        self._tail = None

    def isEmpty(self):
        return self._head == None

    def getHead(self):
        return self._head

    #往链表头添加数据
    def add(self, value):
        self._tail = self._head
        newnode = Node(value, None)
        newnode.setNext(self._head)
        self._head = newnode

    #往链表尾添加数据
    def append(self, value):
        newnode = Node(value)
        if self.isEmpty():
            self._head = newnode
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newnode)
        self._tail = newnode

    def printlist(self):
        list = []
        current = self._head
        while current != None:
            list.append(current.getValue())
            current = current.getNext()
        print(list)
