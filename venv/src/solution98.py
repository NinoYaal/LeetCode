# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         验证二叉搜索树
# Author:       Nino
# Date:         2020/11/4
# Note:
# -------------------------------------------------------------------------------
from tree import *
class Solution:
    def isValidBST(self, root):
        # # val1 val2表示一个取值区间起始于正负无穷，根据左边必然小于根节点，右边必然大于根节点持续更新区间
        # val1, val2 = float('-inf'), float('inf')
        #
        # def f(root, val1, val2):
        #     if not root:
        #         return True
        #     # 若根节点越界返回false
        #     if root.val <= val1 or root.val >= val2:
        #         return False
        #
        #     # 左子树一直小于此时根节点与先前根节点的最小值，右子树一直大于此时根节点与先前根节点的最大值
        #     if not f(root.right, root.val, val2): return False
        #     if not f(root.left, val1, root.val): return False
        #     return True
        #
        # return f(root, val1, val2)
        # 中序遍历
        self.maxmium = float('-inf')
        def bfs(root):
            if not root:
                return True

            if not bfs(root.left):
                return False

            if root.val <= self.maxmium:
                return False
            self.maxmium = root.val

            return bfs(root.right)

        return bfs(root)
if __name__ == "__main__":
    objectName = Solution()
    head = createTree()
    print(objectName.isValidBST(head))
