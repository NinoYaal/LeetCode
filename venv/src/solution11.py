# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         盛最多水的容器
# Author:       Nino
# Date:         2020/11/2
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def maxArea(self, height):
        #双指针分别在最左最右向中间扩展,同时纪录最大面积 时间复杂度O（n）空间复杂度O（1）
        i, j = 0, len(height)-1
        area = 0
        while i < j:
            if height[i] < height[j]:
                area = max(area, height[i]* (j - i))
                i += 1
            else:
                area = max(area, height[j] * (j - i))
                j -= 1
        return area
if __name__ == "__main__":
    objectName = Solution()

    print(objectName.maxArea([1,8,6,2,5,4,8,3,7]))
