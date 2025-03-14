# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict
n = int(input())
birth_death = [tuple(map(int,input().split())) for _ in range(n)]

event = defaultdict(int)
for b,d in birth_death:
    event[b] += 1
    event[d] -= 1

event = dict(sorted(event.items()))

max_people = 0
year = 0
curr_population =0

for y in event:
    curr_population += event[y]
    if curr_population > max_people:
        max_people = curr_population
        year = y
print(year,max_people)