#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# 定义节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 定义链表
class LinkedList:
    def __init__(self):
        self.head = None   # 初始时链表为空

    # 添加节点到链表尾部
    def append(self,data):
        new_node = ListNode(data)
        if not self.head:   # 如果链表为空，新的节点作为头节点
            self.head = new_node
            return
        # 否则遍历到链表尾部，添加新节点
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # 打印链表内容
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# 原链表删除目标元素
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head


# 虚拟头节点法，这样删除和增添操作都是统一起来的
class Solution2:
    def removeElements(self,head,val):
        dummy_head = ListNode()
        dummy_head.next = head
        curr = dummy_head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy_head.next



# @lc code=end

