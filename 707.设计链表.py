#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1
        
        curr = self.dummy_head.next
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.dummy_head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: # 允许尾插
            return
        
        new_node = ListNode(val)
        curr = self.dummy_head  # 插入的节点在第index个位置
        for _ in range(index):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return  
            
        curr = self.dummy_head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

