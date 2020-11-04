# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         调整数组顺序使奇数位于偶数前面
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def exchange(self, nums):
        #双指针，偶数指针从头开始，奇数指针从尾开始
        even, odd = 0, len(nums)-1
        if not nums:
            return nums
        while even < odd:
            while even < len(nums) and nums[even] % 2 != 0:

                even += 1
            while odd >= 0 and nums[odd] % 2 == 0:
                odd -= 1

            if even >= odd:
                break
            nums[even], nums[odd] = nums[odd],nums[even]
        return nums
if __name__ == "__main__":
    objectName = Solution()
    nums = [2,2,2,2]
    print(objectName.exchange(nums))
