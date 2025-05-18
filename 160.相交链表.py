#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 先求长，尾部对齐，再历遍
        countA, countB = 0, 0
        curr = headA
        while curr:
            curr = curr.next
            countA += 1
        curr = headB
        while curr:
            curr = curr.next
            countB += 1
        
        currA = headA
        currB = headB
        if countA >= countB:
            for _ in range(countA-countB):
                currA = currA.next
        else:
            for _ in range(countB-countA):
                currB = currB.next
        
        while currA:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None


# @lc code=end

