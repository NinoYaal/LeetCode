# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         数组中的最长山脉
# Author:       Nino
# Date:         2020/10/25
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def longestMountain(self, A):
        dp1 = [1] + [0] * (len(A)-1)
        dp2 = [0] * (len(A)-1) + [1]
        print(dp1)
        print(dp2)
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                dp1[i] = dp1[i-1] + 1
            else:
                dp1[i] = 1

        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                dp2[i] = dp2[i+1] + 1
            else:
                dp2[i] = 1
        max_len = 0
        for i in range(len(A)):
            if dp1[i] >1 and dp2[i]>1:
                max_len = max(max_len, dp1[i]+dp2[i]-1)

        if max_len >= 3:
            return max_len
        else:
            return 0


if __name__ == "__main__":
    objectName = Solution()
    A = [0,1,0]
    print(objectName.longestMountain(A))
