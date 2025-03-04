# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_r = 0
        count_l = 0
        max_substring = 0
        for letter in s:
            if letter == "R":
                count_r += 1
            else:
                count_l += 1
            if count_l == count_r:
                max_substring += 1
                count_l = 0
                count_r = 0
        return max_substring