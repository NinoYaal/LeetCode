# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         数组中重复的数字
# Author:       Nino
# Date:         2020/10/31
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def findRepeatNumber(self, nums):
        # #使用集合排查
        # hashtable = set()
        #
        # for num in nums:
        #     if  num in hashtable:
        #         return num
        #     else:
        #         hashtable.add(num)
        #
        # 直接修改下标
        for i, num in enumerate(nums):
            while(i != nums[num]):
                if num == nums[num]:
                    return num
                nums[i], nums[num] = nums[num],nums[i]
        return

if __name__ == "__main__":
    objectName = Solution()
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(objectName.findRepeatNumber(nums))
