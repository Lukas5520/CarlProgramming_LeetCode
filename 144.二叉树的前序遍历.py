#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 使用递归的方法
class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []

        def dfs(root):
            if root:
                li.append(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return li
        
# 迭代的写法
class Solution3:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        li = []

        # 我们这里保持遍历的结构统一
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                li.append(node.val)
                # 这里的左右孩子不仅仅是节点，而是左右子树，两个子问题。先进栈的子问题后处理。
                # 栈保证了处理两个子问题的顺序，也就是递归
                if node.right:
                    stack.append(node.right)
                if node.left: 
                    stack.append(node.left)
        return li
    
# 统一的写法
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        stack = [(root, False)] if root else [] 

        while stack:
            node, visited = stack.pop() 
            
            if visited: 
                values.append(node.val)
                continue

            if node.right:
                stack.append((node.right, False))

            if node.left:
                stack.append((node.left, False)) 

            stack.append((node, True))

        return values
            
# @lc code=end

