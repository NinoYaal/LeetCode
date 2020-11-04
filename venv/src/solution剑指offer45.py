# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         把数组排成最小的数
# Author:       Nino
# Date:         2020/11/2
# Note:
# -------------------------------------------------------------------------------
class cmp(str):
    def __lt__(self, other):
        return self + other < other + self

class Solution(object):
    def minNumber(self, nums):
        nums = sorted( [str(i) for i in nums] , key=cmp)
        return "".join(nums)


if __name__ == "__main__":
    objectName = Solution()

    print(objectName.minNumber([10,2]))
