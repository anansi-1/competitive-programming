# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    freq_arr = [0] * 100
    for num in arr:
        freq_arr[num] += 1
    return freq_arr