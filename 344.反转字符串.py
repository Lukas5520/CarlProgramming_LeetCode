#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start

# 一种朴素的想法，其实这就是双指针
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            temp = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = temp

# @lc code=end

