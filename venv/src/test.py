# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         Test
# Author:       Nino
# Date:         2020/10/29
# Note:         仅做测试用
# -------------------------------------------------------------------------------
class Solution:
    def test(self,s):
        if s == '':
            return s
        while s != '' and s[0] == ' ' :
            s = s[1:]
        while s != '' and s[-1] == ' ' :
            s = s[:-1]
        return s


if __name__ == "__main__":
    objectName = Solution()
    s = '    '
    print(objectName.test(s))