#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start

# KMP
class Solution:
    def build_next(self, s: str) -> list:
        n = len(s)
        next = [0 for _ in range(n)]
        j = 0 # 指向最长前缀的末尾
        for i in range(1, n):
            while s[i] != s[j] and j > 0:
                j = next[j-1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

        return next

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        next = self.build_next(needle)
        j = 0 # 指向needle中的字母
        i = 0 # 指向haystack中的字母
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = next[j-1]
                else:
                    i += 1
            
            if j == len(needle):
                return i - j
            
        return -1




# 暴力比对
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        N, n = len(haystack), len(needle)
        if n > N:
            return -1

        for i in range(N):
            if haystack[i] == needle[0]:
                j = i
                k = 0
                state = True

                while state and j<N-1 and k<n-1:
                    j += 1
                    k += 1
                    if haystack[j] != needle[k]:
                        state = False
                        break

                if state and k == n-1:
                    return i
        
        return -1



# @lc code=end

