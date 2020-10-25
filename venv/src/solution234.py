# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         回文链表
# Author:       Nino
# Date:         2020/10/23
# Note:
# -------------------------------------------------------------------------------
from Linkedlist import *
class Solution:
    def isPalindrome(self, head):
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node._value)
            current_node = current_node._next
        return vals == vals[::-1]

if __name__ == "__main__":
    objectName = Solution()
    newLinkedlist = Linkedlist()
    newLinkedlist.append(1)
    newLinkedlist.append(2)
    newLinkedlist.append(2)
    newLinkedlist.append(1)
    print(objectName.isPalindrome(newLinkedlist.getHead()))
