# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         求1+2+...+n
# Author:       Nino
# Date:         2020/10/30
# Note:         不能使用乘除法，循环，判断等，这个条件一出来基本只考虑位运算,逻辑短路与递归
# -------------------------------------------------------------------------------
class Solution:
    def __init__(self):
        self.sum = 0

    def sumNums(self, n):
        #若要用递归实现则判断结束条件需要用上位运算或者逻辑运算符号
        #使用逻辑运算符短路与 短路或

        n >0 and self.sumNums(n - 1)
        self.sum += n
        return self.sum
if __name__ == "__main__":
    objectName = Solution()
    print(objectName.sumNums(100))
