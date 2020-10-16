# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         拥有最多糖果的孩子
# Author:       Nino
# Date:         2020/10/16
# -------------------------------------------------------------------------------
class solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return(ret)

if __name__ == "__main__":
    objectName = solution()
    candypossesslist = [2,3,5,1,3]
    n = 2
    print(objectName.kidsWithCandies(candypossesslist, n))
