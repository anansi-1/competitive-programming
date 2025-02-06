# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for num in range(len(nums)-1):
            if nums[num] == nums[num+1]:
                nums[num]= nums[num+1]*2
                nums[num+1] = 0

        i = 0
        j=0
        for i in range(len(nums)):
            if nums[j] != 0:
                j += 1
            elif nums[j] == 0:
                if nums[i] != 0:
                    nums[i],nums[j] = nums[j],nums[i]
                    j += 1
        return nums