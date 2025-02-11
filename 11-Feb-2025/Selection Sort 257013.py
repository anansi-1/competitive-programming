# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n): # 0 1 2 3 4
            min = i
            for j in range(i+1,n):
                if arr[j] < arr[i]:
                    min = j
                    arr[i],arr[j] = arr[j],arr[i]
        return arr