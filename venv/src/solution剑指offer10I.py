# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         斐波那契数列
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def fib(self,n):
        # #维护一个数组来记录递归过程中已经计算过的值
        # ans = 0
        # fiblist = [0] * (n+1)
        # if n < 1:
        #     return 0
        #
        # def f(n):
        #     if n < 2:
        #         return n
        #     if fiblist[n] > 0:
        #         return fiblist[n]
        #     fiblist[n] = (f(n-1) + f(n-2))% (1e9 + 7)
        #     return fiblist[n]
        # ans = f(n)
        # return int(ans)
        # 动态规划
        if n <= 1:
            return n
        x, y= 0 , 1
        for i in range(2,n+1):
            z = (x + y) % (1e9 + 7)
            x = y
            y = z
        return int(z)
if __name__ == "__main__":
    objectName = Solution()

    print(objectName.fib(100))
