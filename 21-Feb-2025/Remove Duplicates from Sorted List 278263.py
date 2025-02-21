# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        s = set()
        curr,prev = head,head
        while curr:
            if curr.val in s:
                prev.next = curr.next
                curr = curr.next
            else:
                s.add(curr.val)
                prev = curr
                curr = curr.next
        return head