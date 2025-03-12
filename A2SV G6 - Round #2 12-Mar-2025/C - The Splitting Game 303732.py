# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    r = Counter(s)
    l = Counter()
    maxx_sum = 0      
    for i in s:
        l[i] += 1
        r[i] -= 1
        if r[i] == 0:
            del r[i]
        curr_sum = len(l) + len(r)
        maxx_sum = max(maxx_sum, curr_sum)
    print(maxx_sum)