# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dict = defaultdict(list)
        for path in paths:
            s = path.split()
            folder = s[0]
            for f in s[1:]:
                filename,filecontent = f.split(".txt")
                path_dict[filecontent].append(folder + "/" + filename + ".txt")
        ans = []
        for i in path_dict:
            if len(path_dict[i]) > 1:
                ans.append(path_dict[i])
        return ans
        