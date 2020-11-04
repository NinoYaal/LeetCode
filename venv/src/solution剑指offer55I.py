# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         二叉树的深度
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
from tree import *
class Solution:
    def maxDepth(self, root):
        # #深度优先
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return max(dfs(root.left)+1,dfs(root.right)+1)
        # return dfs(root)
        # 广度优先
        if not root:
            return 0
        queue, depth = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            depth += 1
        return depth

if __name__ == "__main__":
    objectName = Solution()
    root = createTree()
    print(objectName.maxDepth(root))
