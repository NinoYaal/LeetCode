# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         删除排序数组中的重复项
# Author:       Nino
# Date:         2020/11/2
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def removeDuplicates(self, nums):
        #双指针i，j。 i指向操作完后数组的最后一位，j遍历整个数组寻找不重复的数字
        i , j =  0, 1
        for j in range(len(nums)):
            #若i，j对应数字相同，则j+1继续寻找不重复数字
            #若i，j对应数字不同，则交换i+1 与j位
            #防止无意义操作，只有在j-i>1才进行交换
            if nums[i] != nums[j]:
                if j - i > 1:
                    nums[i+1] = nums[j]
                i = i + 1
        return nums[:i+1]

if __name__ == "__main__":
    objectName = Solution()
    nums = [1,  2]
    print(objectName.removeDuplicates(nums))
