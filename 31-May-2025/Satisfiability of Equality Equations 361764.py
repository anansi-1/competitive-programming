# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        d = {}
        def find(x):
            if x not in d:
                return x
            else:
                return find(d[x])
        for i in equations:
            if i[1]=="=":
                a = i[0]
                b = i[-1]
                x = find(a)
                y = find(b)
                if x!=y:
                    d[y] = x
        for i in equations:
            if i[1]=="!" and find(i[0])==find(i[-1]):
                return False
        return True