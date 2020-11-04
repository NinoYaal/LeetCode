# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         不用加减乘除做加法
# Author:       Nino
# Date:         2020/11/3
# Note:         位运算
# -------------------------------------------------------------------------------
class Solution:
    def add(self, a, b):
        x = 0xffffffff
        a, b = a & x, b & x
        def f(a,b):
            if b == 0:
                return a
            a, b = a ^ b,(a & b) << 1 & x
            return f(a, b)
        return f(a,b) if f(a,b) <= 0x7fffffff else ~(f(a,b) ^ x)

if __name__ == "__main__":
    objectName = Solution()

    print(objectName.add(-2,1))
