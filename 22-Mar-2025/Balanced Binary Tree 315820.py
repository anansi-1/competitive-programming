# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0
            curr_left = helper(root.left)
            if curr_left == -1:
                return -1
            curr_right = helper(root.right)
            if curr_right == -1:
                return -1
            if abs(curr_left-curr_right) > 1:
                return -1
            return  1 + max(curr_left,curr_right)
        return helper(root) != -1
       