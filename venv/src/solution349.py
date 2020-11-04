# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         两个数的交集
# Author:       Nino
# Date:         2020/11/2
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
if __name__ == "__main__":
    objectName = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(objectName.intersection(nums1,nums2))
