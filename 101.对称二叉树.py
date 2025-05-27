#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 需要收集左右孩子的信息，向上一层返回，后序遍历
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def compare(left,right):
            if not left and not right:
                return True
            elif left and not right:
                return False
            elif not left and right:
                return False
            elif left.val != right.val:
                return False
            else:
                outside_boolen = compare(left.left, right.right)
                inside_boolen = compare(left.right, right.left)
                res = outside_boolen and inside_boolen
                return res
        
        return compare(root.left, root.right)
        
        

        
# @lc code=end

