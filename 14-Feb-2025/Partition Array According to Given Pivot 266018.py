# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        pivot_count = 0
        ans = []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                pivot_count += 1
        for i in range(len(left)):
            ans.append(left[i])
        for p in range(pivot_count):
            ans.append(pivot)
        for j in range(len(right)):
            ans.append(right[j])
        return ans