# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r,ans = [1]*n,[1]*n,[1]*n
        l[0] = nums[0]
        r[-1] = nums[-1]

        for i in range(1,n):
            l[i] = l[i-1]*nums[i]
        for j in range(n-2,-1,-1):
            r[j] = r[j+1]*nums[j]
        
        ans[0] = r[1]
        ans[-1] = l[-2]
        for i in range(1,n-1):
            ans[i] = l[i-1]*r[i+1]
        return ans
        
