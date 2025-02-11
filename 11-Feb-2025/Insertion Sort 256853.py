# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    for i in range(1,n):
        cur = arr[i]
        j = i -1
        while j >= 0 and arr[j] > cur:
            arr[j+1] = arr[j]
            print(" ".join(map(str,arr)))
            j -= 1
        arr[j+1] = cur
    print(" ".join(map(str,arr)))