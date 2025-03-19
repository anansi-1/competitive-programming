# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
            if not root:
                return []
            queue = deque([root])
            ans = [root.val]
            while queue:
                temp = []
                curr = len(queue)
                for i in range(curr):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                        temp.append(node.left.val)
                    if node.right:
                        queue.append(node.right)
                        temp.append(node.right.val)
                if temp:
                    ans.append(max(temp))
            return ans