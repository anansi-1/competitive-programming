# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            curr_level = []
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.popleft()
                curr_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if count%2 != 0:
                l,r = 0,len(curr_level) - 1
                while l < r:
                    curr_level[l].val,curr_level[r].val = curr_level[r].val,curr_level[l].val
                    l += 1
                    r -= 1
            count += 1
        return root


