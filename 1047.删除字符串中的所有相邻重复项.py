#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for x in s:
            if len(stack) == 0 or x != stack[-1]:
                stack.append(x)
            else:
                stack.pop()
        
        return ''.join(stack)

# @lc code=end

