# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        is_open = False
        stack = []
        count = 0
        for i in s:
            if i == "(":
                is_open = True
                stack.append(i)
            else:
                if is_open:
                    count += 2**(len(stack)-1)
                    is_open = False
                stack.pop()
        return count
