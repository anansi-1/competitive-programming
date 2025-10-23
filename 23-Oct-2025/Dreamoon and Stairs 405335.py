# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

n, m = map(int, input().split())
i = 0
if n < m :
    print(-1)
else :
    while n > 0 :
        n -= 2*m
        i += 1
    print(m*i)