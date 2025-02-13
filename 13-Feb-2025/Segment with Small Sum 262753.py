# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,s = map(int,input().split())
arr = list(map(int,input().split()))
max_len = 0
cur_len = 0
tot_sum = 0
l = 0
for r in range(len(arr)): 
    tot_sum += arr[r]
    cur_len += 1
    while tot_sum > s:
         tot_sum -= arr[l]
         cur_len -= 1
         l += 1
    max_len = max(cur_len,max_len)

print(max_len)