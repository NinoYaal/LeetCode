# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         顺时针打印矩阵
# Author:       Nino
# Date:         2020/10/30
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def spiralOrder(self, matrix):
        # 深度优先从头开始走,
        # ans = []
        # if not matrix or not matrix[0]:
        #     return ans
        # #建立一个辅助矩阵来纪录是否访问过
        # n = len(matrix)
        # m = len(matrix[0])
        # visited = [[False] *m for i in range(n)]
        #
        # #设定上下左右四个方向( 右下左上 )
        # directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # direction = 0
        # #初始条件设置
        # row, col = 0,0
        # nextrow, nextcol = 0,0
        # #从头开始模拟遍历整个matrix
        # for i in range(n*m):
        #     ans.append(matrix[row][col])
        #     visited[row][col] = True
        #     nextrow, nextcol = row+ directions[direction][0], col + directions[direction][1]
        #     if not( 0 <= nextrow < n and 0 <= nextcol < m and not visited[nextrow][nextcol]):
        #         direction = (direction + 1) % 4
        #     row += directions[direction][0]
        #     col += directions[direction][1]
        # return ans
        #按层模拟
        #打出最外层后 递归打印下一个子矩阵
        ans = []
        if not matrix or not matrix[0]:
            return ans
        row, col = len(matrix) , len(matrix[0])
        #定义外圈的index top,bottom,left,right
        top, bottom, left, right = 0, row-1 , 0,  col -1
        while top <= bottom and left <= right:
            #最上面一行
            for c in range(left, right+1):
                print(c)
                ans.append(matrix[top][c])
            #从第二行开始到最下面一行的一列
            for r in range(top+1, bottom+1):
                ans.append(matrix[r][right])
            #判断是否子矩阵只剩一行
            if top < bottom and left < right:
                #最下面一行从倒数第二列开始到第一列
                for c in range(right-1, left, -1):
                    ans.append(matrix[bottom][c])
                #从倒数第二行开始到最上面一行的一列
                for r in range(bottom-1, top, -1):
                    ans.append(matrix[r][left])
            top += 1
            bottom -= 1
            left+=1
            right-=1
        return ans
if __name__ == "__main__":
    objectName = Solution()
    matrix = [[9, 10, 11, 12]]
    print(objectName.spiralOrder(matrix))
