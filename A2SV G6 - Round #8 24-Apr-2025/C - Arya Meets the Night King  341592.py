# Problem: C - Arya Meets the Night King  - https://codeforces.com/gym/599383/problem/C

s,b = map(int,input().split())
a = list(map(int,input().split()))
d_g = []
for _ in range(b):
    curr= (tuple(map(int,input().split())))
    d_g.append(curr)
d_g.sort()
gold_so_far = 0
k = []
defense_gold = {}
def get_index(attack_power,k):
    curr = -1
    left = 0 
    right = len(k) - 1
    while left <= right:
        mid = (left + right)//2
        if k[mid] <= attack_power:
            curr = k[mid]
            left = mid + 1
        else:
            right = mid - 1
    return curr

for defense,gold in d_g:
    gold_so_far += gold
    k.append(defense)
    defense_gold[defense] = gold_so_far

ans = []
for i in a :
    idx = get_index(i,k)
    if idx == -1:
        ans.append(0)
    else:
        ans.append(defense_gold[idx])
print(*ans)