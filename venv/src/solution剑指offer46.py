# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         把数字翻译成字符串
# Author:       Nino
# Date:         2020/10/30
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def translateNum(self, num):
        numlist = list(map(int,str(num)))
        dp = [1] * (len(numlist)+1)
        #分析一下dp[i] 增加的条件，如果该位置上的数字大于5，则该数字只能被单独翻译，可翻译次数不增加
        #若该位置与前一位的组合数字大于等于10 小于等于25时能被联合翻译，否则只能单个翻译
        #当该位置被单独翻译时，次数为f（i）=f（i-1）
        #当该位置能与前一位联动翻译时，次数为 f（i）=f（i-1）+ f（i-2）
        for i in range(2,len(numlist)+1):
            curNum = 10 * numlist[i-2]+ numlist[i-1]
            if  curNum >= 10 and curNum <= 25:
                if i == 1 :
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]
if __name__ == "__main__":
    objectName = Solution()
    num = 12
    print(objectName.translateNum(num))
