# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
            def recursiveSearch(nums,low,high,target):
                if low > high:
                    return -1
                mid = (low+high)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return recursiveSearch(nums,low,mid-1,target)
                else:
                    return recursiveSearch(nums,mid+1,high,target)
            return recursiveSearch(nums,0,len(nums)-1,target)