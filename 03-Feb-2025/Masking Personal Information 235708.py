# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = s.split("@")
            for i in range(2):
                s[i] = s[i].lower()
            name = list(s[0])
            s[0] = name[0] + "*"*5 + name[-1]
            ans = "@".join(s)
            return ans
        else:
            separation = "+-(), "
            number = []
            for i in s:
                if i in separation:
                    continue
                number.append(i)
            mask = ""
            if len(number) == 10:
                mask = "***-***-"
            elif len(number) == 11:
                mask = "+*-***-***-"
            elif len(number) == 12:
                mask = "+**-***-***-"
            elif len(number) == 13:
                mask = "+***-***-***-"
            number = number[-4:]
            print(number)
            number = "".join(number)
            ans = mask + number
            return ans