# Problem: Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        current=head
        previous=dummy
        while current:
            c=0
            while current.next and current.val==current.next.val:
                current=current.next
                c+=1
            if c>0:
                previous.next=current.next
            else:
                previous=previous.next
            current=current.next
        return dummy.next