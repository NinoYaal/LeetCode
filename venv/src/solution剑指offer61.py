# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         扑克牌中的顺子
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def isStraight(self, nums):
        # 设置一个大王小王计数器,最大值最小值计数器,以及一个去重，不含大小王的set
        min, max = float("inf"), 0
        num_set = set()
        count0 = 0
        for num in nums:
            if num == 0:
                count0 += 1
                continue
            if num < min:
                min = num
            if num > max:
                max = num
            num_set.add(num)

        if max - min >= 5:
            return False
        if len(num_set)+count0 != 5:
            return  False,num_set
        return True,max,min


if __name__ == "__main__":
    objectName = Solution()
    nums = [9,4,2,5,6]
    print(objectName.isStraight(nums))
