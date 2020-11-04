# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         有效的山脉数组
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def validMountainArray(self, A):
        #两个指针i，j分别从头尾开始遍历数组A 只要出现后一位比前一位小就返回false
        if len(A) <= 2:
            return False
        i, j = 0, len(A)-1
        for l in range(len(A)):
            if i < len(A)-1 and A[i+1]>A[i] :
                i += 1
            if j > 0 and A[j-1] > A[j]:
                j -=1
        return i == j and i > 0 and j < len(A)-1

if __name__ == "__main__":
    objectName = Solution()
    A = [3,5,6]
    print(objectName.validMountainArray(A))
