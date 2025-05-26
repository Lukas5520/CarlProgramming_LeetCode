#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []

        def dfs(root):
            if root:
                dfs(root.left)
                li.append(root.val)
                dfs(root.right)

        dfs(root)
        return li
    

# 迭代的写法
class Solution3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # 中序遍历 [[left],root,[right]]
        # 这个stack就是要缓存我们的一串root，
        # 等到左边问题处理完，从stack中弹出元素，再处理它的右子问题
        stack = []
        li = []
        curr = root

        # 直到某一右子问题解决完毕，且没有待处理子问题，结束
        while curr or stack:
            # 先迭代访问最底层的左子树节点
            if curr:
                stack.append(curr)
                curr = curr.left
            # 到达最左节点后处理栈顶节点 
            else:
                curr = stack.pop() # 中
                li.append(curr.val)
                curr = curr.right
        return li
            
            
# 统一的写法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        stack = [(root, False)] if root else [] # 多加一个参数，False 为默认值，含义见下文

        while stack:
            node, visited = stack.pop() # 多加一个 visited 参数，使“迭代统一写法”成为一件简单的事
            
            if visited: # visited 为 True，表示该节点和两个儿子的位次之前已经安排过了，现在可以收割节点了
                values.append(node.val)
                continue

            # visited 当前为 False, 表示初次访问本节点，此次访问的目的是“把自己和两个儿子在栈中安排好位次”。
            # 中序遍历是'左中右'，右儿子最先入栈，最后出栈。
            if node.right:
                stack.append((node.right, False))

            stack.append((node, True)) # 把自己加回到栈中，位置居中。同时，设置 visited 为 True，表示下次再访问本节点时，允许收割

            if node.left:
                stack.append((node.left, False)) # 左儿子最后入栈，最先出栈

        return values


# @lc code=end

