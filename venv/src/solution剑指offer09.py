# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         用两个栈实现队列
# Author:       Nino
# Date:         2020/10/31
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def __init__(self):
        self.stackin = []
        self.stackout = []
    def appendTail(self, value):
        self.stackin.append(value)

    def deleteHead(self):
        if self.stackout:
            return self.stackout.pop()
        else:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        if not self.stackout:
            return -1
        else:
            return self.stackout.pop()
if __name__ == "__main__":
    objectName = Solution()
    objectName.appendTail(3)
    print(objectName.deleteHead())
    print(objectName.deleteHead())
