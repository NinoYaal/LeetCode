# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         查找常用字符
# Author:       Nino
# Date:         2020/10/27
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def commonChars(self, A):
        count = [float('inf')] * 26
        for word in A:
            charfrequency = [0] * 26
            for char in word:
                charfrequency[ord(char) - ord('a')] += 1
            for i in range(26):
                count[i] = min(count[i],charfrequency[i])
        ans = list()
        for i in range(26):
            ans.extend([chr(i + ord('a'))] * count[i])
        return ans


if __name__ == "__main__":
    objectName = Solution()
    A = ["bella","label","roller"]
    print(objectName.commonChars(A))
