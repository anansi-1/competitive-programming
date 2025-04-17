# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left,right):
            if left>right:
                return 0
            num_left=nums[left]-helper(left+1,right)
            num_right=nums[right]-helper(left,right-1)
            return max(num_left,num_right)

        res=helper(0,len(nums)-1)
        return res>=0