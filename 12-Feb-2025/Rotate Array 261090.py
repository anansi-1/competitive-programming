# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k): # 0 1 2
            to_be_added = nums.pop()
            nums.insert(0,to_be_added)
        return nums
