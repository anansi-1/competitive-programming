# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join(map(str,digits)))
        digits += 1
        ans = []
        for digit in str(digits):
            ans.append(int(digit))
        return ans

