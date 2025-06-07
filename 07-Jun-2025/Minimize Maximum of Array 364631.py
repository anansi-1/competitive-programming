# Problem: Minimize Maximum of Array - https://leetcode.com/problems/minimize-maximum-of-array/

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        answer = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            curr = math.ceil(prefix_sum / (i + 1))
            answer = max(answer, curr)
        return answer