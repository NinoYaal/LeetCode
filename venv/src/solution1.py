# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         两数之和
# Author:       Nino
# Date:         2020/10/25
# Note:         对时间复杂度最好的诠释以及对hashtable最朴实的应用
# -------------------------------------------------------------------------------
class Solution:
    # def twoSum(self, nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return[i,j]
    #     return
    def twoSum(self, nums, target):
        hashtable = dict()
        for i,num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable [nums[i]] = i
        return []
if __name__ == "__main__":
    objectName = Solution()
    nums = [2,3,5,67,7,32,11]
    print(objectName.twoSum(nums,9))
