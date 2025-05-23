#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        self.instack.append(x)

    def pop(self) -> int:
        # 复用empty函数
        if self.empty():
            return None
        
        # 列表的pop()既删除末尾值又将其返回
        if self.outstack:
            return self.outstack.pop()
        else:
            for _ in range(len(self.instack)):
                temp = self.instack.pop()
                self.outstack.append(temp)
            return self.outstack.pop()
            
    def peek(self) -> int:
        # 出队列，再将出来的元素放回到outstack
        temp = self.pop()
        self.outstack.append(temp)
        return temp

    def empty(self) -> bool:
        if not self.instack and not self.outstack:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

