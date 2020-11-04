# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         青蛙跳台阶问题
# Author:       Nino
# Date:         2020/11/1
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def numWays(self, n):
        # # 1 直接递归，多次重复，时间复杂度O（2^n）
        # ans = 0
        #
        # def feibonaqi(n):
        #     if n < 2:
        #         return 1
        #     return feibonaqi(n - 1) + feibonaqi(n - 2)
        #
        # ans = feibonaqi(n)
        # return ans
        # 递归中纪录数据直接使用
        ans = 0
        fab = [0] * (n + 1)

        def feibonaqi(n):
            if n < 2:
                return 1
            if fab[n] > 0:
                return fab[n]
            fab[n] = (feibonaqi(n - 1) + feibonaqi(n - 2)) % (1e9 + 7)
            return fab[n]

        ans = feibonaqi(n)
        # for i,num in enumerate(fab):
        #     fab[i] = int(fab[i] % (1e9 + 7))
        return int(ans)


if __name__ == "__main__":
    objectName = Solution()
    n = 2
    print(objectName.numWays(n))
