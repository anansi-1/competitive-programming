# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

from collections import defaultdict
t = int(input())
points = [tuple(map(int,input().split())) for _ in range(t)]

coordinate = defaultdict(int)

for l,r in points:
    coordinate[l] += 1
    coordinate[r+1] -= 1
keys = sorted(coordinate.keys())
coverage = 0
prev = keys[0]
result = defaultdict(int)
for point in keys:
    result[coverage] += point - prev
    coverage += coordinate[point]
    prev = point
for k in range(1,t+1):
    print(result[k],end=" ")