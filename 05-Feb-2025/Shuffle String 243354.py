# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        order = {}
        ans = []
        for letter,index in zip(s,indices):
            order[index] = letter
        for i in range(len((s))):
            ans.append(order[i])
        return "".join(ans)
        

