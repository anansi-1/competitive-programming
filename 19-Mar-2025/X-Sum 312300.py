# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    diag1 = {}  
    diag2 = {}  
    for i in range(n):
        for j in range(m):
            if (i - j) not in diag1:
                diag1[i - j] = 0
            if (i + j) not in diag2:
                diag2[i + j] = 0
            diag1[i - j] += mat[i][j]
            diag2[i + j] += mat[i][j]
    maxx = 0
    for i in range(n):
        for j in range(m):
            total_sum = diag1[i - j] + diag2[i + j] - mat[i][j]
            maxx = max(maxx, total_sum)
    print(maxx)
