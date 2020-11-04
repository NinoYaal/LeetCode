# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 储存栈，辅助栈
        self.A = list()
        self.B = list()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)
        else:
            self.B.append(self.B[-1])
    def pop(self):
        """
        :rtype: None
        """
        self.A.pop()
        self.B.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]
    def min(self):
        """
        :rtype: int
        """
        return  self.B[-1]

if __name__ == "__main__":
    objectName = Solution()
    objectName.push(-2)
    objectName.push(0)
    objectName.push(-3)
    print(objectName.min())
    print(objectName.pop())
    print(objectName.top())
