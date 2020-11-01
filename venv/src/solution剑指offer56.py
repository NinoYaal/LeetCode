# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         数组中数字出现次数I
# Author:       Nino
# Date:         2020/10/30
# Note:         要求O（n）时间O（1）空间
# -------------------------------------------------------------------------------
class Solution:
    def singleNumbers(self, nums):
        # #排序后用栈 排序时间为ologn 不符合要求
        # nums.sort()
        # ans = []
        # for num in nums:
        #     if ans and ans[-1] == num:
        #         ans.pop()
        #     else:
        #         ans.append(num)
        # return ans
        # 异或运算
        ans = 0
        a = 0
        b = 0
        for n in nums:
            ans ^= n
        
        return ans

if __name__ == "__main__":
    objectName = Solution()
    nums = [4,1,4,6]
    print(objectName.singleNumbers(nums))
