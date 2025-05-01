# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = []
        while head:
            n.append(head.val)
            head = head.next
        n.sort()
        dummy = ListNode(0)
        curr = dummy
        for val in n:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next