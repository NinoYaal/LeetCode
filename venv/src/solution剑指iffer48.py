# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         最长不含重复字符的子字符串
# Author:       Nino
# Date:         2020/10/31
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):
        #动态规划
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        str = list(s)
        hashtable = dict()
        hashtable[s[0]] = 0
        for i in range(1, len(str)):
            if s[i] not in hashtable:
                hashtable[s[i]] = i
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = min(i - hashtable[s[i]], dp[i-1]+1)
                hashtable[s[i]] = i
        ans = max(dp)
        return dp
if __name__ == "__main__":
    objectName = Solution()
    s = 'abba'
    print(objectName.lengthOfLongestSubstring(s))
