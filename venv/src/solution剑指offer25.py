# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         合并两个排序的链表
# Author:       Nino
# Date:         2020/11/1
# Note:
# -------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Linkedlist import *
class Solution:
    def mergeTwoLists(self, l1, l2):
        newhead = dumhead = Node()
        while l1 and l2:
            if l1.val >= l2.val:
                newhead.next = l2
                l2 = l2.next
            else:
                newhead.next = l1
                l1 = l1.next
            newhead = newhead.next
        newhead.next = l1 if l1 else l2
        return dumhead.next
if __name__ == "__main__":
    objectName = Solution()
    l1 = Node(1,Node(2,Node(4,None)))
    l2 = Node(1,Node(3,Node(5,None)))
    print(objectName.mergeTwoLists(l1,l2))
