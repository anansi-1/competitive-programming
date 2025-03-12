# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n,k = map(int,input().split())
arr = list(map(int,input().split()))
curr = sum(arr[:k])
t = curr
for i in range(k,n):
    curr += arr[i] - arr[i-k]
    t += curr
print(t/ (n-k+1))