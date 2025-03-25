# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        starting = -1
        ending = -1
        def start(nums,target):
            nonlocal starting
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (r+l)//2
                if nums[mid] == target:
                    starting = mid
                    if mid == 0:
                        return starting
                    l = 0
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return starting
        def end(nums,target):
            nonlocal ending
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (r+l)//2
                if nums[mid] == target:
                    ending = mid
                    if mid == len(nums)-1:
                        return ending
                    l = mid + 1
                    r = len(nums) - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ending
        return [start(nums,target),end(nums,target)]