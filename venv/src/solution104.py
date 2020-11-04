# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         二叉树的最大深度
# Author:       Nino
# Date:         2020/11/4
# Note:
# -------------------------------------------------------------------------------
from tree import *
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)

if __name__ == "__main__":
    objectName = Solution()
    head = createTree()
    print(objectName.maxDepth(head))
