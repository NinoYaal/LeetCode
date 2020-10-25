# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         比较含退格的字符串
# Author:       Nino
# Date:         2020/10/19
# Note:
# -------------------------------------------------------------------------------
class solution:
    def backspaceCompare(self, S, T):
        news = self.removeBackspace(S)
        newt = self.removeBackspace(T)
        return news == newt


    def removeBackspace(self, S):
        news = []
        for char in S:
            if char == '#':
                if not len(news) == 0:
                    news.pop()
                continue
            news.append(char)
        s = ''.join(news)
        return s
if __name__ == "__main__":
    objectName = solution()
    S = "ab#c"
    T = "ad#c"
    print(objectName.backspaceCompare(S, T))
