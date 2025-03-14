# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort() 
    a_index = []
    ans = [0]*len(a)
    for i in range(len(a)):
        a_index.append((a[i],i))
    a_index.sort()
    for i in range(len(b)):
        idx = a_index[i][1]
        ans[idx] = b[i]
    for i in ans:
        print(i,end=" ")
    print()