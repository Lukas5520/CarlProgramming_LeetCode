#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # 结果要么循环出现，要么变为1
        # 维护一个数组记录所有出现的值，查询元素是否在数组中是O(1)的
        values = []
        while True:
            square_sum = 0
            for s in str(n):
                square_sum += int(s) ** 2

            if square_sum == 1:
                return True
            if square_sum in values:
                return False
            else:
                n = square_sum
                values.append(n)
# @lc code=end

