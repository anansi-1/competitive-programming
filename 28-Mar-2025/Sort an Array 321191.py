# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        l,r = 0,0
        curr_arr = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                curr_arr.append(left[l])
                l += 1
            else:
                curr_arr.append(right[r])
                r += 1
        while l < len(left):
            curr_arr.append(left[l])
            l += 1
        while r < len(right):
            curr_arr.append(right[r])
            r += 1
        return curr_arr