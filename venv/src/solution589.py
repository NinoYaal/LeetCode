# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         N叉树的前序遍历
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from tree import *
class Solution:
    def preorder(self, root):
        ans = list()
        def f(root):
            if not root:
                return
            ans.append(root.val)
            for child in root.children:
                f(child)
        f(root)
        return ans

if __name__ == "__main__":
    objectName = Solution()
    root = NtreeNode(1,[NtreeNode(3,[NtreeNode(5),NtreeNode(6)]),NtreeNode(2),NtreeNode(4)])
    print(objectName.preorder(root))
