# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        to_be_added = 0
        l = l1
        r = l2

        ans = ListNode(None)
        head = ans
        while l and r:
            val_sum = l.val + r.val + to_be_added
            ans.next = ListNode(val_sum%10)
            to_be_added = val_sum//10
            l = l.next
            r = r.next
            ans = ans.next
        while l:
            val_sum = l.val + to_be_added
            ans.next = ListNode(val_sum%10)
            to_be_added = val_sum//10
            l = l.next
            ans = ans.next
        while r:
            val_sum = r.val + to_be_added
            ans.next = ListNode(val_sum%10)
            to_be_added = val_sum//10
            r = r.next
            ans = ans.next
        if to_be_added != 0:
            ans.next = ListNode(to_be_added)
        return head.next