# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         传递信息
# Author:       Nino
# Date:         2020/10/27
# Note:
# -------------------------------------------------------------------------------
import collections
class Solution:
    # 深度优先dps
    #时间复杂度：O(n^k)
    #空间复杂度：O(n)。
    # def numWays(self, n, relation, k):
    #     self.n,self.k,self.ans = n, k, 0
    #     self.dict = collections.defaultdict(list)
    #     for x,y in relation:
    #         self.dict[x].append(y)
    #     self.search(0,0)
    #     return self.ans
    # def search(self, index, num):
    #     if num == self.k:
    #         if index == self.n - 1:
    #             self.ans += 1
    #         return
    #
    #     for i in self.dict[index]:
    #         self.search(i, num + 1)
    #动态规划
    def numWays(self, n, relation, k):
        dp = [[0]*n for c in range(k+1)]
        dp[0][0] = 1
        for c in range(k):
            for x,y in relation:
                dp[c+1][y] += dp[c][x]
        return dp[k][n-1]



if __name__ == "__main__":
    objectName = Solution()
    print(objectName.numWays(5,[[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]],3))
