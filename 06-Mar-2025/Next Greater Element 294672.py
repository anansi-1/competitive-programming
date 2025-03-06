# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            idx = nums2.index(i)
            if idx+1 > len(nums2)-1:
                ans.append(-1)
                continue
            for j in range(idx+1,len(nums2)):
                if nums2[j]>i:
                    ans.append(nums2[j])
                    break 
                elif j >= len(nums2)-1:
                    ans.append(-1)
        return ans