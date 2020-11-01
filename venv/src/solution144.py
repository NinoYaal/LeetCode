# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         二叉树的前序遍历
# Author:       Nino
# Date:         2020/10/28
# Note:
# -------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree import *
class Solution:
    def preorderTraversal(self, root):
        #使用递归
        #
        # def preorder(root):
        #     if root == None:
        #         return
        #     ans.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        # ans = list()
        # preorder(root)
        # return ans
        # 使用迭代
        ans = list()
        stack = list()
        if root == None:
            return []
        stack.append(root)

        while len(stack) != 0:
            current = stack.pop()
            ans.append(current.val)
            if current.right != None:
                stack.append(current.right)
            if current.left != None:
                stack.append(current.left)

        return ans

if __name__ == "__main__":
    objectName = Solution()
    tree = TreeNode('A', TreeNode('B', TreeNode('D'), TreeNode('E')), TreeNode('C'))
    print(objectName.preorderTraversal(tree))
