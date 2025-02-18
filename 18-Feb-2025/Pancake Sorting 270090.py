# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        def flip(i):
            for j in range(0,i//2+1):
                arr[j],arr[i-j] = arr[i-j],arr[j]

        for i in range(len(arr)-1, 0, -1): 
            for j in range(1, i+1): 
                if arr[j] == i+1:
                        flip(j)
                        result.append(j+1)
                        break
            flip(i)
            result.append(i+1)
        return result