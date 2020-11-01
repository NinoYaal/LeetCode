# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         独一无二的出现次数
# Author:       Nino
# Date:         2020/10/28
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def uniqueOccurrences(self, arr):
        return len(set(collections.Counter(arr).values())) == len(set(arr))

if __name__ == "__main__":
    objectName = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    print(objectName.uniqueOccurrences(arr))
