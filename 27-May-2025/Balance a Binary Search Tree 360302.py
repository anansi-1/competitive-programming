# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(node):
            if node:
                inorder(node.left)
                nums.append(node.val)
                inorder(node.right)
        def bst(l, r):
            if l > r:
                return None
            mid = l + (r - l) // 2
            root = TreeNode(nums[mid])
            root.left = bst(l, mid - 1)
            root.right = bst(mid + 1, r)
            return root
        inorder(root)
        return bst(0, len(nums) - 1)