# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
a = [int(i) for i in input().split()]
a1 = sorted(a)
b1  = [0] * (n + 1)
b2 = [0] * (n + 1)
for i in range(n):
    b1[i + 1] = b1[i] + a[i]
    b2[i + 1] = b2[i] + a1[i]
m = int(input())
for i in range(m):
    t, l, r = [int(i) for i in input().split()]
    if t == 1:
        print(b1[r] - b1[l - 1])
    else:
        print(b2[r] - b2[l - 1])