#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start

# 能通过大部分测试，但是运行超时，可能是-nums[i]-nums[j] in nums[j+1:]导致的
# class Solution0:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         nums.sort()
#         ans = []

#         # 去重: 更新指针时跳过重复的值
#         for i in range(n-1):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1,n):
#                 # 这里j也要往回判断
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     continue
#                 if -nums[i]-nums[j] in nums[j+1:]:
#                     ans.append([nums[i],nums[j],-nums[i]-nums[j]])
#         return ans

# 双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n-2):
            if nums[i] > 0:
                return ans
            # [-4,-1,-1,0,1,2]
            # 先i++再往回判断，不然会跳过第一个-1漏解
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    ans.append([nums[i],nums[left],nums[right]])

                    # 这样写导致死循环
                    # while left < right:
                    #     if nums[left] == nums[left+1]:
                    #         left += 1
                    #     if nums[right] == nums[right-1]:
                    #         right -= 1

                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1

        return ans        

# @lc code=end

