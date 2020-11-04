# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         括号生成
# Author:       Nino
# Date:         2020/11/4
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def generateParenthesis(self, n):
        l, r = n, n
        res = []

        # 未被弹出的右括号数量必须大于等于左括号，若r == l,则必须弹出左括号
        def popStacks(tmp, l, r):
            if l == 0 and r == 0:
                res.append(tmp)
                return
            if l > 0:
                popStacks(tmp + '(', l - 1, r)
            if r > l:
                popStacks(tmp + ')', l, r - 1)
        popStacks('', l, r)
        return res
if __name__ == "__main__":
    objectName = Solution()

    print(objectName.generateParenthesis(4))
