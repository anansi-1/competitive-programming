# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        current = head
        while current is not None:
            list.append(current.val)
            current = current.next
        i = 0
        j = len(list) - 1
        while i < j:
            if list[i] != list[j]:
                return False
            i += 1
            j -= 1
        return True