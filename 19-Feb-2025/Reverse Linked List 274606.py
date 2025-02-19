# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        curr = head
        temp = curr.next
        next_temp =curr.next.next
        curr.next = None
        while next_temp != None:
            temp.next = curr
            curr = temp
            temp = next_temp
            next_temp = next_temp.next
        temp.next = curr

        return temp
   