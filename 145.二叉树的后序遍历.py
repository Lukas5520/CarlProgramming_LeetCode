#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归的写法
class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                li.append(root.val)

        dfs(root)

        return li
    

# 迭代的写法
class Solution3:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        li = []

        stack.append(root)
        # 前序[root,[left],[right]]
        # 后序[[left],[right],root]
        # 只需要将[root,[right],[left]]倒序
        while stack:
            node = stack.pop()
            if node:
                li.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        li.reverse()
        return li

# 统一的写法
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        stack = [(root, False)] if root else [] # 多加一个参数，False 为默认值，含义见下文

        while stack:
            node, visited = stack.pop() # 多加一个 visited 参数，使“迭代统一写法”成为一件简单的事
            
            if visited: # visited 为 True，表示该节点和两个儿子的位次之前已经安排过了，现在可以收割节点了
                values.append(node.val)
                continue

            stack.append((node, True))

            if node.right:
                stack.append((node.right, False))

            if node.left:
                stack.append((node.left, False)) 

        return values                    
# @lc code=end

