#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        # 遇到左括号入栈，遇到右括号出栈对应
        stack = []
        for x in s:
            if x == '(':
                stack.append(')')
            elif x == '[':
                stack.append(']')
            elif x == '{':
                stack.append('}')
            # 三种情况：左括号多，右括号多，不对应匹配
            elif len(stack) == 0 or x != stack[-1]: # 处理了右括号多、不对应匹配两种情况
                return False
            else:
                stack.pop()

        if len(stack) != 0:
            return False
        else:
            return True

# 方法二，使用字典
class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item: 
                return False
            else: 
                stack.pop()
        return True if not stack else False
# @lc code=end

