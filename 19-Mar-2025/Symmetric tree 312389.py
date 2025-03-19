# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node_l,node_r):
            if node_l == None and node_r == None:
                return True
            elif node_l == None or node_r == None:
                return False
            c_one = helper(node_l.left,node_r.right)
            c_two = helper(node_l.right,node_r.left)
            return node_l.val == node_r.val and c_one and c_two
        return helper(root.left,root.right)