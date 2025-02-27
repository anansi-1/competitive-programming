# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))
c=defaultdict(int)
l=0
l2,r2=0,0
for r in range(n):
    c[arr[r]]+=1
    while len(c)>k:
        c[arr[l]]-=1
        if c[arr[l]]==0:
            del c[arr[l]]
        l+=1
    if (r-l)>(r2-l2):
        l2,r2=l,r
print(l2+1,r2+1)