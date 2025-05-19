#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}  # 用来存放遍历过的元素
        for idx, num in enumerate(nums):
            if target - num in table:
                return [idx,table[target - num]]
            table[num] = idx

# @lc code=end

