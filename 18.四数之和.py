#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n-3):
            if nums[i] > target and (target > 0 or nums[i] > 0):
                break
            if i>0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,n-2):
                if nums[i]+nums[j]>target and (target>0 or nums[i]+nums[j]>0):
                    break
                if j>i+1 and nums[j] == nums[j-1]:
                    continue

                left, right = j+1, n-1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum > target:
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
            
        return ans
                


# @lc code=end

