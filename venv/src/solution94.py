# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         二叉树的中序遍历
# Author:       Nino
# Date:         2020/11/3
# Note:         要求用迭代算法完成
# -------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from tree import  *
class Solution:
    def inorderTraversal(self, root):
        #1 递归
        # ans = []
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     ans.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return ans
        # 迭代， 将所有左子节点压入栈中直到不存在子节点
        # 此时弹出最后压入栈中的子节点并查看是否存在右子节点，若存在则以右子节点为新的根节点来压入左子节点
        # 若不存在右节点则继续从栈中弹出节点，直到栈为空
        ans = list()
        if not root:
            return
        stack = list()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans

if __name__ == "__main__":
    objectName = Solution()
    root = TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))
    print(objectName.inorderTraversal(root))
