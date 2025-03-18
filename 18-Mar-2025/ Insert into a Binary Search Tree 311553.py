# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
       
        if root == None:
            return TreeNode(val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        return root
        

        '''
        insert(4,5).right =  insert(7,5)
        insert(7,5).left =  insert(None,5)
        insert(None,5) <-- TreeNode(5)

        insert(4,5).right =  insert(7,5)
        insert(7,5).left =  5
        insert(None,5) <-- TreeNode(5)


        '''