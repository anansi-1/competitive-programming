# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        count=0
        odd=0
        l=0
        for r in range(len(nums)):
            if nums[r]%2==1:
                odd+=1
                count=0
            while odd==k:
                if nums[l]%2==1:
                    odd-=1
                count+=1
                l+=1
            res+=count
        return res