# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

ans = []
i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        ans.append(arr1[i])
        i += 1
    else:
        ans.append(arr2[j])
        j += 1

while i < len(arr1):
    ans.append(arr1[i])
    i += 1
while j < len(arr2):
    ans.append(arr2[j])
    j += 1

print(" ".join(map(str,ans)))