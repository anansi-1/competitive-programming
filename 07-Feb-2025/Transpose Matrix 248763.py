# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
            rows = len(matrix)
            cols = len(matrix[0])

            ans = []
            for i in range(cols):
                row = []
                for j in range(rows):
                    row.append(matrix[j][i])
                ans.append(row)
            return ans
