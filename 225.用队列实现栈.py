#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
from collections import deque
class MyStack:

    def __init__(self):
        # deque是双向队列，只使用append()和popleft()表示进队和出队
        self.Q = deque()
  
    def push(self, x: int) -> None:
        self.Q.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        
        for _ in range(len(self.Q) - 1):
            self.Q.append(self.Q.popleft())
        return self.Q.popleft()
    
    def top(self) -> int:
        ans = self.pop()
        self.Q.append(ans)
        return ans

    def empty(self) -> bool:
        return len(self.Q) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

