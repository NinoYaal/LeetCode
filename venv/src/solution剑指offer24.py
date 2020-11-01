# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         反转链表
# Author:       Nino
# Date:         2020/10/31
# Note:
# -------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Linkedlist import *
class Solution:
    def reverseList(self, head):
        #双指针
        # if head == None or head.next == None:
        #     return head
        #
        # cur = head
        # pre = None
        # while cur:
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        #
        # return pre
        # 递归
        if head == None or head.next == None:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead
if __name__ == "__main__":
    objectName = Solution()
    list = Node(1,Node(2,(Node(3,Node(4,Node(5,None))))))
    print(objectName.reverseList(list))
