# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         每个元音包含偶数次的最长子字符串
# Author:       Nino
# Date:         2020/10/23
# Note:         由于只考虑元音奇偶次数 ，使用二进制来纪录起到压缩状态的作用。 aeiou 分别 对应 00001，00010，00100，01000，10000
#               其中0，1分别对应偶数次与奇数次。那么一共就会有32种状态。使用 dp来纪录这32种状态下对应的最长的字符串长度 最后取max获得
#               最长字符串长度
# -------------------------------------------------------------------------------
class Solution:
    def findTheLongestSubstring(self, s):
        #初始化一个dp数组来纪录32种状态下的长度
        dp =[-1] +[-float('inf')]*31
        pattern = 0
        ans = 0
        for i,char in enumerate(s):
            #通过异或操作来获得状态值
            if char == 'a':
                pattern ^= 1 << 0
            elif char == 'e':
                pattern ^= 1 << 1
            elif char == 'i':
                pattern ^= 1 << 2
            elif char == 'o':
                pattern ^= 1 << 3
            elif char == 'u':
                pattern ^= 1 << 4
            # 纪录或者更新当前pattern状态下的最长长度
            # 若该pattern首次出现，则直接更新此状引所处长度索引（也就是更新这个pattern的起始点）。若该状态非首次出现则要对比出现这段pattern增加的长度 i - dp[pattern] 与
            # 原来已经保存的最长长度的长短然后更新答案
            if dp[pattern] != -float('inf'):
                ans = max(ans, i - dp[pattern])
            else:
                dp[pattern] = i
        return ans


if __name__ == "__main__":
    objectName = Solution()
    s = 'eleetminicoworoep'
    print(objectName.findTheLongestSubstring(s))
