# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         二叉树
# Author:       Nino
# Date:         2020/10/23
# Note:
# -------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class NtreeNode(object):
    def __init__(self, val=0, children = []):
        self.val = val
        self.children = children

def createTree():
    return TreeNode(3,TreeNode(3,TreeNode(3)),TreeNode(4,TreeNode(3,TreeNode(3,TreeNode(3)))))