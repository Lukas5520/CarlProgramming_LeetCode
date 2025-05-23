#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start

# python中str不可变，必须开新空间
# 先去掉多余空格，再整个反转字符串，最后反转每个单词的字母
# (版本四) ：将字符串转换为列表后，使用双指针去除空格

# class Solution:
#     def single_reverse(self, s, start: int, end: int):
#         n = end - start
#         for i in range(n//2):
#             s[start+i], s[end-i-1] = s[end-i-1], s[start+i]

#     def reverseWords(self, s: str) -> str:
#         s = list(s)
#         s.reverse()

#         result = ""
#         fast = 0
#         while fast < len(s):
#             if s[fast] != " ":
#                 if len(result) != 0:
#                     result += " "
#                 while s[fast] != " " and fast < len(s):
#                     result += s[fast]
#                     fast += 1
#             else:
#                 fast += 1

#         # 逐个单词翻转
#         slow, fast = 0, 0
#         while fast <= len(s)-1:
#             while s[fast] != ' ':
#                 fast += 1
#             self.single_reverse(s,slow,fast)
#             slow, fast = fast+1, fast+1
            
class Solution:
    def single_reverse(self, s, start: int, end: int):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        result = ""
        fast = 0
        # 1. 首先将原字符串反转并且除掉空格, 并且加入到新的字符串当中
        # 由于Python字符串的不可变性，因此只能转换为列表进行处理
        s = list(s)
        s.reverse()
        while fast < len(s):
            if s[fast] != " ":
                if len(result) != 0:
                    result += " "
                while s[fast] != " " and fast < len(s):
                    result += s[fast]
                    fast += 1
            else:
                fast += 1
        # 2.其次将每个单词进行翻转操作
        slow = 0
        fast = 0
        result = list(result)
        while fast <= len(result):
            if fast == len(result) or result[fast] == " ":
                self.single_reverse(result, slow, fast - 1)
                slow = fast + 1
                fast += 1
            else:
                fast += 1

        return "".join(result)        
# @lc code=end

