# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         字符串的排列
# Author:       Nino
# Date:         2020/10/30
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def permutation(self, s):
        #通过回溯剪枝的方法来枚举所有可能的排列方案
        # ans = []
        # str = list(s)
        #深度优先搜索把符合条件的字符合并到答案里，最后将答案添加到列表里
        # def dfs(index):
        #     if index == len(str)-1 :
        #         ans.append(''.join(str))
        #         return
        #     replicate = set()
        #     for i in range(index,len(str)):
        #         if str[i] in replicate: continue
        #         replicate.add(str[i])
        #         str[index], str[i] = str[i], str[index]
        #         dfs(index+1)
        #         str[index], str[i] = str[i], str[index]
        # dfs(0)

        #用切片来代替交换，整体思路相同
        ans = []
        def backtrack(s, element):
            if not s:
                ans.append(element)
            replicate = set()
            for i in range(len(s)):
                if s[i] in replicate: continue
                replicate.add(s[i])
                backtrack(s[:i]+ s[i+1:],element + s[i])
        backtrack(s,'')
        return  ans

if __name__ == "__main__":
    objectName = Solution()
    s = "abc"
    print(objectName.permutation(s))
