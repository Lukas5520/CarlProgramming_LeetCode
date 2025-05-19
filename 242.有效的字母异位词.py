#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0 for _ in range(26)]
        for i in t:
            record[ord(i)-ord('a')] += 1
        for i in s:
            record[ord(i)-ord('a')] -= 1
        for i in record:
            if i != 0:
                return False
        return True
# @lc code=end

