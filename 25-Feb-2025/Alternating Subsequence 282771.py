# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

testcases=int(input())
for _ in range(testcases):
    n=int(input())
    nums=list(map(int,input().split()))  
    i=0
    max_sum=0
    while i<len(nums):
        max_value=nums[i]
        while i+1<len(nums) and nums[i]*nums[i+1]>0:
            max_value=max(max_value,nums[i+1])
            i+=1
        max_sum+=max_value
        i+=1   
    print(max_sum)
