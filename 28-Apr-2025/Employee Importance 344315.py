# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(e):
            imp = emp[e].importance
            for s in emp[e].subordinates:
                imp += dfs(s)
            return imp
        emp = {}
        for e in employees:
            emp[e.id] = e
        return dfs(id)
