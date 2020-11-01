# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         最大子序和
# Author:       Nino
# Date:         2020/10/29
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def maxSubArray(self, nums):
        #动态规划优化
        #不使用一个dp数组来储存每个位置的值而是直接用一个temp值一直记录当前位置的最大值
        #空间复杂度O（1） 时间复杂度O（n）
        ans = nums[0]
        temp = 0
        for num in nums:
            temp = max(num, temp+num)
            ans = max(temp, ans)
        return ans

if __name__ == "__main__":
    objectName = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(objectName.maxSubArray(nums))
