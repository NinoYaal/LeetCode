# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         速算机器人
# Author:       Nino
# Date:         2020/10/25
# Note:         起始值x = 1，y = 0
# -------------------------------------------------------------------------------
class Solution:
    # def calculate(self, s):
    #     x = 1
    #     y = 0
    #     for char in s:
    #         if char == 'A':
    #             x *= 2
    #             x += y
    #         if char == 'B':
    #             y *= 2
    #             y += x
    #     return x+y
    def calculate(self, s):
        return 2 ** len(s)
if __name__ ==  "__main__":
    objectName = Solution()
    s = 'ABA'
    print(objectName.calculate(s))

