# Problem: Shifting Letters - https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def shift(letter, num):
            num = (ord(letter) - ord('a') + num) % 26  
            return chr(num + ord('a'))

        to_be_added = [0] * len(shifts)

        for i in range(len(shifts)):
            to_be_added[0] += shifts[i]
            if i + 1 < len(shifts):
                to_be_added[i + 1] -= shifts[i]

        for i in range(1, len(to_be_added)):
            to_be_added[i] += to_be_added[i - 1]

        for i in range(len(to_be_added)):
            to_be_added[i] = shift(s[i], to_be_added[i])

        return "".join(to_be_added)