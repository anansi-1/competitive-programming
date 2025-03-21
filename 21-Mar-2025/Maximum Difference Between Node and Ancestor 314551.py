# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root,curr_max,curr_min):
            nonlocal res
            if not root:
                return
            curr_max = max(curr_max,root.val)
            curr_min = min(curr_min,root.val)
            res = max(res,abs(curr_max-root.val),abs(curr_min-root.val))
            helper(root.left,curr_max,curr_min)
            helper(root.right,curr_max,curr_min)
        helper(root,root.val,root.val)
        return res

        
            