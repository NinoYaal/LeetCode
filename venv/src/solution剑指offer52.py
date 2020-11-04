# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         两个链表的第一个公共节点
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Linkedlist import *
class Solution:
    def getIntersectionNode(self, headA, headB):
        # #集合法
        # cur = headA
        # node_set = set()
        # while cur:
        #     node_set.add(cur)
        #     cur = cur.next
        # while headB:
        #     if headB in node_set:
        #         return headB.val
        #     headB = headB.next
        # return
        # 双指针
        if not headA or not headB:
            return
        aptr = headA
        bptr = headB

        while aptr != bptr:
            aptr = aptr.next if aptr else headB
            bptr = bptr.next if bptr else headA
        return aptr
if __name__ == "__main__":
    objectName = Solution()
    Nodea1 = Node(3)
    Nodea2 = Node(4)
    Nodea1.next = Nodea2

    Nodeb1 = Node(2)
    Nodeb2 = Node(8)
    Nodeb3 = Node(10)
    Nodeb1.next = Nodeb2
    Nodeb2.next = Nodeb3

    Nodec1 = Node(5,Node(7,Node(9)))
    Nodea2.next = Nodec1
    Nodeb3.next = Nodec1
    print(objectName.getIntersectionNode(Nodea1, Nodeb1))
