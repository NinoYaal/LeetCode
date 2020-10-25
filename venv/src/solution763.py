# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         划分字母区间
# Author:       Nino
# Date:         2020/10/22
# Note:         小写字母组成的字符串，划分的区间数量尽可能多
# -------------------------------------------------------------------------------
class solution:
    def partitionLabels(self, S):
        label_index = [0] * 26
        #纪录所有的字母最后出现的位置
        for index, label in enumerate(S):
            label_index[ord(label) - ord('a')] = index
        #从左到右遍历字符串每到一个尽可能小的截取点截取片段

        #字符串的开始与结束
        start = 0
        end = 0
        newlists = list()
        for i in range(len(S)):
            end = max(end, label_index[ord(S[i])- ord('a')])
            if i == end:
                newlists.append(end - start +1)
                start = end + 1

        return newlists
if __name__ == "__main__":
    objectName = solution()
    S = 'ababcbacadefegdehijhklij'
    print(objectName.partitionLabels(S))
