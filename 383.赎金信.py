#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for char in magazine:
            if char in magazine_count:
                magazine_count[char] += 1

        for char in ransomNote:
            if magazine_count.get(char, 0) == 0:
                return False
            magazine_count[char] -= 1

        return True
# @lc code=end

