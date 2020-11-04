# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         链表中倒数第k个节点
# Author:       Nino
# Date:         2020/11/2
# Note:
# -------------------------------------------------------------------------------
from Linkedlist import *
class Solution:
    def getKthFromEnd(self, head, k):
        # cur = head
        # if not head or k == 0:
        #     return
        # length  = 0
        # while head:
        #     length += 1
        #     head = head.next
        # if k > length:
        #     return
        # for i in range(length-k):
        #     cur = cur.next
        # return cur
        # 双指针 让前指针比后指针慢k步
        if not head or k == 0:
            return
        former, latter = head, head
        for i in range(k):
            if not latter:return
            latter = latter.next
        while latter:
            former = former.next
            latter = latter.next
        return former

if __name__ == "__main__":
    objectName = Solution()
    head = Node(1,Node(2,Node(3,Node(4,Node(5,None)))))
    print(objectName.getKthFromEnd(head,2))
