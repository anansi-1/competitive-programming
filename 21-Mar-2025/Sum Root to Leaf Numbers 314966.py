# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def helper(root,curr_num):
            if not root:
                return
            if not root.left and not root.right:
                ans.append(curr_num*10 + root.val)
                return
            curr_num = curr_num*10 + root.val
            helper(root.left,curr_num)
            helper(root.right,curr_num)
        helper(root,0)
        return sum(ans)