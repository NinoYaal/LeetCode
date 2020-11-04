# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         和为s的两个数字
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def twoSum(self, nums, target):
        # #暴力搜索，从头开始，一个个找匹配
        # for num in nums:
        #     if num > target:
        #         return []
        #     if target - num in nums:
        #         return [num, target-num]
        # hashmap遍历数组 对于数字x 如果target-x 在hash表中，返回解。否则纪录该数字
        # hashmap = dict()
        # for num in nums:
        #     if target - num in hashmap:
        #         return [num, target - num]
        #     else:
        #         hashmap[num] = 1
        # return []
        # 双指针 左右指针分别从头尾开始，若和大于target 则右指针左移，否则 左指针右移
        if len(nums) == 1:
            return []
        left, right = 0, len(nums) -1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [nums[left], nums[right]]
        return []

if __name__ == "__main__":
    objectName = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(objectName.twoSum(nums,target))
