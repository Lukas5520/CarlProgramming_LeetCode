#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归的写法
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 前序遍历
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 每次递归调用 invertTree 都返回当前子树的根节点（root），
        # 但这个返回值一般不会被递归调用的上层使用，
        # 只有最初的调用（即最外层调用）会拿这个返回值来作为最终结果。
        return root
        

class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 中序遍历
        self.invertTree(root.left)

        temp = root.left
        root.left = root.right
        root.right = temp
        
        # 处理交换之后的左子树，相当于是原来的右子树
        self.invertTree(root.left)

        return root
        
# @lc code=end

