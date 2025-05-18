#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 双指针版本
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 双指针初始化
        pre = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        return pre


# @lc code=end

