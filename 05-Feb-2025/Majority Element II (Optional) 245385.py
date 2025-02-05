# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

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