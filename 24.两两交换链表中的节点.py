#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)
        curr = dummy_head
        while curr.next and curr.next.next: # 判断顺序不能反，否则会报错空指针
            temp = curr.next
            curr.next = curr.next.next
            temp.next = curr.next.next
            curr.next.next = temp

            curr = curr.next.next

        return dummy_head.next
# @lc code=end

