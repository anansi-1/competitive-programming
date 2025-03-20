# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        count = 0
        def helper(node):
            nonlocal max_depth, count
            if not node:
                return   
            count += 1 
            helper(node.left)  
            max_depth = max(max_depth, count)  
            helper(node.right)  
            count -= 1 

        helper(root)
        return max_depth

