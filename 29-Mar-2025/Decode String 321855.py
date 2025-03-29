# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ']':
                char = ''
                count = ''
                while stack and stack[-1] != '[':
                    char = stack.pop() + char
                stack.pop()
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                ans = int(count) * char
                stack.extend(ans)
                continue
            else:
                stack.append(i)
        return "".join(stack)