# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         有多少小于当前数字的数字
# Author:       Nino
# Date:         2020/10/26
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # 快速排序+hash
        sortnums = sorted(nums)
        hashtable = dict()
        for i,num in enumerate(sortnums):
            if num not in hashtable:
                hashtable[num] = i
        ans = list()

        for n in nums:
            ans.append(hashtable[n])
        return ans

        # 桶排序
        # bucket = [[0,i] for i in range(101)]
        # for num in nums:
        #     bucket[num][0] +=1
        # count = [0]
        # for i in range(1,len(bucket)):
        #     count.append(count[i-1]+bucket[i-1][0])
        # ans = []
        # for num in nums:
        #     ans.append(count[num])
        # return ans
        # 暴搜
        # ans = []
        # for i,numone in enumerate(nums):
        #     count = 0
        #     for j,numtwo in enumerate(nums):
        #         if numtwo < numone:
        #             count+= 1
        #     ans.append(count)
        # return ans
if __name__ == "__main__":
    objectName = Solution()
    nums = [7,2,4,5,3]
    print(objectName.smallerNumbersThanCurrent(nums))
