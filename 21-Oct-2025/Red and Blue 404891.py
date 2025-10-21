# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for i in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input(). split()))
    r.append(0)
    b.append(0)
    maxr,maxb = 0,0 
    for i in range(1, len(r)):
        r[i] += r[i-1]
        maxr=max(maxr, r[i-1])
    for i in range(1, len(b)):
        b[i] += b[i-1]
        maxb=max(maxb, b[i-1])
    print(maxb+maxr)