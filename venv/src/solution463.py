# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         岛屿的周长
# Author:       Nino
# Date:         2020/10/30
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def islandPerimeter(self, grid):
        ans = 0
        blockCount = 0
        blockrep = 0
        #获得总共的block数量
        #获得相交的block数量
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    blockCount +=1
                    if j < len(grid[0])-1 and grid[i][j + 1] == 1:
                        blockrep += 1
                    if i < len(grid) -1 and grid[i+1][j] == 1:
                        blockrep += 1
        return blockCount *4 - blockrep * 2

if __name__ == "__main__":
    objectName = Solution()
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]

    print(objectName.islandPerimeter(grid))
