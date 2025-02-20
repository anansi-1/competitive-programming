# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        r = head
        count = 0
        while count != n:
            r = r.next
            count += 1
        while r != None:
            prev = l
            r = r.next
            l = l.next
            count += 1
        if n== count:
            head = l.next
            l.next = None
        else:
            prev.next = l.next
        return head