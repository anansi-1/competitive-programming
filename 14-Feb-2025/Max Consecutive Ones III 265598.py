# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

        num_zero = 0
        max_consecutive = 0
        cur_zero = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zero += 1
            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1
            cur_zero = r - l + 1
            max_consecutive = max(max_consecutive,cur_zero)
        return max_consecutive