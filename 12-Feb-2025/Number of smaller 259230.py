# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n,m = map(int,input().split())
arr1 = list(map(int,map(int,input().split())))
arr2 = list(map(int,map(int,input().split())))
ans = []
l,r = 0,0
for num in arr2: 
    while l < len(arr1) and arr1[l] < num: 
        l += 1
    ans.append(l)
print(" ".join(map(str,ans)))