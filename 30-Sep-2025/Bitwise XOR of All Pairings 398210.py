# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        for num in nums1:
            xor1 ^= num
        xor2 = 0
        for num in nums2:
            xor2 ^= num
        if len(nums2) % 2 == 0:
            xor1 = 0
        if len(nums1) % 2 == 0:
            xor2 = 0
        return xor1 ^ xor2
        