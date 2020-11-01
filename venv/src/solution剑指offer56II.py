# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         数组中数字出现的次数II
# Author:       Nino
# Date:         2020/10/30
# Note:         最容易想到的是放进字典里，位运算更快
# -------------------------------------------------------------------------------
class Solution:
    def singleNumber(self, nums):
        # 字典纪录每个数字出现次数然后再遍历一整个字典，时间复杂度O（n）空间复杂度O（n）
        hashtable = dict()
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
                continue
            hashtable[num] = 1
        for key in hashtable:
            if hashtable[key] == 1:
                return key

        #使用位运算

if __name__ == "__main__":
    objectName = Solution()
    nums = [9, 1, 7, 9, 7, 9, 7]
    print(objectName.singleNumber(nums))
