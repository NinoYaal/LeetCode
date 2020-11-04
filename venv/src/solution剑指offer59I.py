# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         滑动窗口的最大值
# Author:       Nino
# Date:         2020/11/3
# Note:         k总是有效的
# -------------------------------------------------------------------------------
class Solution:
    def maxSlidingWindow(self, nums, k):
        # # 给定窗口区间为[i,j], 最大值为max，每移动一格，多一格nums[j+1] 少一格nums[i] 最大值需要重新遍历3个格子，暴力法
        # if not nums:
        #     return []
        # maxs = [0] * (len(nums) - k + 1)
        # i, j = 0, k - 1
        # while j < len(nums):
        #     maxs[i] = max([nums[l] for l in range(i, i + k)])
        #     i += 1
        #     j += 1
        # return maxs
        #
if __name__ == "__main__":
    objectName = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(objectName.maxSlidingWindow(nums,k))
