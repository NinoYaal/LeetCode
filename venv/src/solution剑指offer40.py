# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         最小的k个数
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def getLeastNumbers(self, arr, k):
        if k > len(arr):
            return arr
        arr.sort()
        return arr[:k]
if __name__ == "__main__":
    objectName = Solution()
    arr = [3, 2, 1]
    k = 2
    print(objectName.getLeastNumbers(arr,k))
