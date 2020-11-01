# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         
# Author:       Nino
# Date:         2020/10/31
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def maxSubArray(self, nums):
        #动态规划
        ans = nums[0]
        curMax = 0
        for i, num in enumerate(nums):
            curMax = max(num, curMax+num)
            ans = max(ans, curMax)
        return  ans
if __name__ == "__main__":
    objectName = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(objectName.maxSubArray(nums))
