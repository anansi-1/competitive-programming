# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

n = int(input())
for _ in range(n):
    m,a= int(input()),list(map(int,input().split()))
    r = 1
    l = 0
    count = 0
    while r < len(a):
        if a[l] > a[r]:
            count += 1
            l += 2
            r += 2
        else:
            l += 1
            r += 1
    print(count)