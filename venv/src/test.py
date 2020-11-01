# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         Test
# Author:       Nino
# Date:         2020/10/29
# Note:
# -------------------------------------------------------------------------------
class Solution:
    def test(self):
        return
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
if __name__ == "__main__":
    objectName = Solution()
    a = (1, [2, 3])
    print(my_abs(12))