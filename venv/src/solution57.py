# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         插入区间
# Author:       Nino
# Date:         2020/11/4
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def insert(self, intervals, newInterval):
        ans = list()
        #假设旧区间的为 [ol,or], 新区间为[nl,nr]。判断重合的方式即有 or >= nl 或者 ol <=  nr。
        #判断完重合即可合并区间，合并出来的新区间为 [min(ol, nl), max(or,nr)]
        placed = False
        for interval in intervals:
            #新区间在区间左边 不重合
            if newInterval[1] < interval[0]:
                if not placed:
                    ans.append(newInterval)
                    placed = True
                ans.append(interval)
            #新区间在区间右边 不重合
            elif newInterval[0] > interval[1]:
                ans.append(interval)
            #重合了，重新计算新区间大小
            else:
                newInterval = [min(interval[0],newInterval[0]),max(interval[1],newInterval[1])]

        if not placed:
            ans.append(newInterval)
        return ans


if __name__ == "__main__":
    objectName = Solution()

    print(objectName.insert( [[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
