#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s not in ['+','-','*','/']:
                stack.append(int(s))
            elif s == '+':
                a = stack.pop()
                b = stack.pop()
                result = b + a
                stack.append(result)
            elif s == '-':
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)
            elif s == '*':
                a = stack.pop()
                b = stack.pop()
                result = b * a
                stack.append(result)
            else :
                a = stack.pop()
                b = stack.pop()
                # //是除完向下取整，int(b/a)才能向零截断
                result = int(b / a)
                stack.append(result)
        
        return stack.pop()
# @lc code=end

