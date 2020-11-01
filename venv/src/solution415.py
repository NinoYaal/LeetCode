# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         字符串相加
# Author:       Nino
# Date:         2020/10/26
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def addStrings(self, num1, num2):
        i, j, carry, ans = len(num1)-1, len(num2)-1, 0,''
        while i>= 0 or j >= 0 or carry:
            c = carry
            if i >= 0:
                i, c = i-1, c+ ord(num1[i])-48
            if j >= 0:
                j, c = j-1, c + ord(num2[j])-48
            carry, c = divmod(c,10)
            ans = str(c)+ ans
        return ans
if __name__ == "__main__":
    objectName = Solution()
    nums1 = '7429'
    nums2 = '24092'
    print(objectName.addStrings(nums1,nums2))
