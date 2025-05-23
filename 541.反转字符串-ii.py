#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == 1:
            return s
        s = list(s)  
        n = len(s)
        batch = 0
        while 2*k*(batch+1) <= n:
            for i in range(k//2):
                s[i+2*k*batch], s[k-i-1+2*k*batch] = s[k-i-1+2*k*batch], s[i+2*k*batch]
            batch += 1
        
        # 我们自己写这个判断有点多
        remaining_count = n - 2*k*batch
        reverse_count = min(remaining_count,k)
        for i in range(reverse_count//2):
            s[i+2*k*batch], s[reverse_count-i-1+2*k*batch] = s[reverse_count-i-1+2*k*batch], s[i+2*k*batch]

        return ''.join(s)  

# @lc code=end

