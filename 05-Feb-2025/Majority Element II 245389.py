# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        print(count)
        for key,value in count.items():
            if value > (len(nums)//3):
                ans.append(key)
        return ans