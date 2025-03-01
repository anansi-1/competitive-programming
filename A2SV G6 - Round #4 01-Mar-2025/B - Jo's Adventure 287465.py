# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n,m = map(int,input().split())
nums = list(map(int,input().split()))
prefix_sum = [0]
suffix_sum = []
for r in range(1,len(nums)):
    if nums[r] < nums[r-1]:
        prefix_sum.append(nums[r-1]-nums[r])
    else:
        prefix_sum.append(0)
for r in range(0,len(nums)-1):
    if nums[r+1] > nums[r]:
        suffix_sum.append(abs(nums[r+1]-nums[r]))
    else:
        suffix_sum.append(0)
suffix_sum.append(0)
for i in range(1,len(prefix_sum)):
    prefix_sum[i] += prefix_sum[i-1]
for i in range(len(suffix_sum)-2,-1,-1):
    suffix_sum[i] += suffix_sum[i+1]
for _ in range(m):
    s,e = (map(int,input().split()))   
    if s < e:
        print(prefix_sum[e-1]-prefix_sum[s-1])
    else:
        print(suffix_sum[e-1]-suffix_sum[s-1])