# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         种花问题
# Author:       Nino
# Date:         2020/11/4
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0

        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 or n == 0 else False
        for i, bed in enumerate(flowerbed):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1
            if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                count += 1
                flowerbed[i] = 1
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1
        return count >= n

if __name__ == "__main__":
    objectName = Solution()

    print(objectName.canPlaceFlowers([1,0,0,0,1],1))
