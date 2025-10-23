# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
l = [0]*(n+1)
for i in range(2,n+1):
    if l[i] == 0:
        for j in range(2*i,n+1,i):
            l[j] += 1
ans = l.count(2)
print(ans)