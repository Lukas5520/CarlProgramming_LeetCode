#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        table = {}
        
        for i in nums1:
            for j in nums2:
                if i+j in table:
                    table[i+j] += 1
                else:
                    table[i+j] = 1

        count = 0
        for i in nums3:
            for j in nums4:
                if 0-(i+j) in table:
                    count += table[0-(i+j)]
        
        return count
# @lc code=end

