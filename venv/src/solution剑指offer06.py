# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         从尾到头打印链表
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
from Linkedlist import *
class Solution:
    def reversePrint(self, head):
        # 递归
        # if not head:
        #     return
        # ans = list()
        # def f(head):
        #     if not head:return
        #     f(head.next)
        #     ans.append(head.val)
        #     return
        # f(head)
        # return ans
        # 切片
        ans = list()
        while head:
            ans.append(head.val)
            head = head.next
        return ans[-1::-1]

if __name__ == "__main__":
    objectName = Solution()
    head = Node(3,Node(5,Node(6)))
    print(objectName.reversePrint(head))
