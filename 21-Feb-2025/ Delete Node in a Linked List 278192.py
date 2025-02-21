# Problem:  Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''
        2 -> 9 -> 1 -> 5 -> 3 -> 6 -> 8 -> 7 -> None
                  c
        2 -> 9 -> 5 -> 5 -> 3 -> 6 -> 8 -> 7 -> None
                  c
        2 -> 9 -> 5 -> 3 -> 6 -> 8 -> 7 -> None
                  c
        '''

        cur = node
        cur.val = cur.next.val
        cur.next = cur.next.next
        
