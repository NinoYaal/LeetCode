# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         反转字符串
# Author:       Nino
# Date:         2020/10/16
# Note:         空间要求O(1)
# -------------------------------------------------------------------------------
class solution:
    def reverseString(self, s):
        mid = int(len(s)/2)
        for i in range(mid):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        return s
if __name__ == "__main__":
    objectName = solution()
    s = ['h','e','l','l','o']
    print(objectName.reverseString(s))
