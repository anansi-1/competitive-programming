# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        l = 0
        r = len(arr) - 1
        max_sum = float('-inf')
        while l < r:
            curr_sum = arr[l] + arr[r]
            max_sum = max(curr_sum,max_sum)
            l += 1
            r -= 1
        return max_sum