# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def helper(root):
            nonlocal ans
            if not root:
                return 0,0
            l,l_count = helper(root.left)
            r, r_count = helper(root.right)
            total = root.val + l + r
            curr_count = 1 + l_count + r_count
            if total // curr_count == root.val:
                ans += 1
            return total,curr_count
        helper(root)
        return ans