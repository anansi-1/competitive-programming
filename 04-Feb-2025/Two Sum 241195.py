# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for num in range(len(nums)):
            curr = nums[num]
            if target-curr in dict:
                return (dict[target-curr],num)
            dict[curr]= num