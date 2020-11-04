# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         和为s的连续正数序列
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def findContinuousSequence(self, target):
        #枚举
        #这个序列的第一位不会超过目标的一半，所以设定一个枚举上限
        #优化方案有使用数学求和公式 然后通过求根公式获得对应开始左边界的右边界
        limit = int(target/2)
        ans = list()
        for i in range(1,limit + 1):
            sum = 0
            start = i
            tmp = list()
            while sum < target:
                sum += start
                tmp.append(start)
                start += 1
                if sum == target:
                    ans.append(tmp)
                    break
                if sum > target:
                    break
        return ans
        #双指针

if __name__ == "__main__":
    objectName = Solution()

    print(objectName.findContinuousSequence(14))
