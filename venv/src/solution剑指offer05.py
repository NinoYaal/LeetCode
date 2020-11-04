# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         替换空格
# Author:       Nino
# Date:         2020/11/3
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def replaceSpace(self, s):
        news = ''.join(('%20' if c == ' ' else c for c in s))
        return news
if __name__ == "__main__":
    objectName = Solution()
    s = "We are  happy."
    print(objectName.replaceSpace(s))
