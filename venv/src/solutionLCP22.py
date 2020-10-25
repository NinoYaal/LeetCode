# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         黑白方格画
# Author:       Nino
# Date:         2020/10/25
# Note:         排列组合的知识
# -------------------------------------------------------------------------------
import math
class Solution:
    def paintingPlan(self, n, k):
        ans = 0
        if k == n*n:
            return 1
        for i in range(n):
            for j in range(n):
                if (n*(i+j) - i*j) == k:
                    ans += self.combination(n,i) * self.combination(n,j)
        return ans
    def combination(self, n, m):
        return int(math.factorial(n)/(math.factorial(m)*math.factorial(n-m)))
if __name__ == "__main__":
    objectName = Solution()

    print(objectName.paintingPlan(2,2))
