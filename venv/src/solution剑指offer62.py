# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         圆圈中最后剩下的数字
# Author:       Nino
# Date:         2020/11/2
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def lastRemaining(self, n, m):
        #递归
        # def f(n, m):
        #     if n == 0:
        #         return 0
        #     return (m+f(n-1,m)) % n
        # return f(n,m)
        #迭代
        f = 0
        for i in range(2,n+1):
            f = (m + f) % i
        return f
if __name__ == "__main__":
    objectName = Solution()

    print(objectName.lastRemaining(5,3))
