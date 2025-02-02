# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(n):          
            if (i+1) % 3 ==0 and (i+1) % 5 == 0:
                 ans.append("FizzBuzz")
            elif (i+1)%3==0:
                 ans.append("Fizz")
            elif (i+1)%5==0:
                 ans.append("Buzz")
            else:
                 ans.append(f"{i + 1}")
        return ans