# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         求根到叶子节点数字之和
# Author:       Nino
# Date:         2020/10/29
# Note:
# -------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree import *
class Solution:
    def sumNumbers(self, root):
        return self.dfs(root, 0)

    def dfs(self, root, i):
        if root == None:
            return 0
        currentVal = i * 10 + root.val
        if root.left == None and root.right == None:
            return currentVal
        return self.dfs(root.left, currentVal) + self.dfs(root.right, currentVal)



if __name__ == "__main__":
    objectName = Solution()
    tree = TreeNode(1, TreeNode(3, TreeNode(4), TreeNode(2)), TreeNode(6))
    print(objectName.sumNumbers(tree))
