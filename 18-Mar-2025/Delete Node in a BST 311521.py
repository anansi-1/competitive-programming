# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            while node.left:
                node = node.left
            return node
        def search(root,key):
            if not root:
                return None
            if key == root.val:
                if root.left == None and root.right == None:
                    return None
                elif root.left != None and root.right == None:
                    root = root.left
                    return root
                elif root.left == None and root.right != None:
                    root = root.right
                    return root
                else:
                    curr = find_min(root.right)
                    root.val = curr.val
                    curr.val = key
                    root.right = search(root.right,key)
                    return root
                    
            elif root.val > key:
                root.left = search(root.left,key)
            elif root.val < key:
                root.right = search(root.right,key)
            return root

        return search(root,key)