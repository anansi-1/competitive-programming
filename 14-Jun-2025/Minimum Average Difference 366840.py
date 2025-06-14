# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pre = []
        sum = 0
        for i in nums:
            sum += i
            pre.append(sum)
        total_sum = sum  
        minn = float('inf')
        for i in range(len(pre)):
            left = pre[i] // (i + 1)  
            if (len(nums) - (i + 1)) > 0:
                right = (total_sum - pre[i]) // (len(nums) - (i + 1))
            else:
                right = 0  
            end = abs(left - right)
            if end <minn:
                id=i
                minn=end
        return id


