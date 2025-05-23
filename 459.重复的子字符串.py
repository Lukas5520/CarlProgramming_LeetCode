#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start

# 我们自己写的
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 首先计算next数组
        n = len(s)
        if n == 0:
            return False
        
        # 我们通常上还是喜欢for的写法
        next = [0 for _ in range(n)]
        j = 0
        i = 1
        while i < n:
            while s[i] != s[j] and j > 0:
                j = next[j-1]
            if s[i] == s[j]:
                next[i] = j + 1
            i += 1
            j += 1

        max_lenth = next[-1]
        if n % (n - max_lenth) == 0 and max_lenth > 0:
            return True
        
        return False


# 一种答案
class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:  
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        if nxt[-1] != 0 and len(s) % (len(s) - nxt[-1]) == 0:
            return True
        return False
    
    def getNext(self, nxt, s):
        nxt[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt
# @lc code=end

