# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        to_be_added = 0
        def helper(root):
            nonlocal to_be_added
            if root == None:
                return 0
            helper(root.right)
            to_be_added += root.val
            root.val = to_be_added
            helper(root.left)
        helper(root)
        return root