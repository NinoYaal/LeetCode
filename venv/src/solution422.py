# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         找到所有数组中消失的数字
# Author:       Nino
# Date:         2020/10/27
# Note:         题目要求了使用O（1）空间，hashmap是O（n）空间。所以要达到要求，可以直接修改数组
# -------------------------------------------------------------------------------
class Solution:
    def findDisappearedNumbers(self, nums):
        # 使用hashmap
        # hashmap = dict()
        # for num in nums:
        #     hashmap[num] = 1
        # ans = list()
        # for num in range(1,len(nums)+1):
        #     if num not in hashmap:
        #         ans.append(num)
        # return ans
        # 直接修改数字对应的索引为负数
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] = -nums[abs(num)-1]
        ans = list()
        for i,num in enumerate(nums):
            if num >0:
                ans.append(i+1)
        return ans

if __name__ == "__main__":
    objectName = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(objectName.findDisappearedNumbers(nums))
