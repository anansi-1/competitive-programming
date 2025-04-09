# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course,pre in prerequisites:
            adj_list[pre].append(course)
        white,gray,black=1,2,3
        color = {course: white for course in range(numCourses)}
        no_cycle = True
        def dfs(node):
            nonlocal no_cycle
            if not no_cycle:
                return
            color[node] = gray
            for n in adj_list[node]:
                if color[n] == white:
                    dfs(n)
                elif color[n] == gray:
                    no_cycle = False
            color[node] = black

        for course in range(numCourses):
            if color[course] == white:
                dfs(course)
        return no_cycle

