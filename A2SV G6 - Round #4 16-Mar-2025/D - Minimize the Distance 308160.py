# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
num = list(map(int,input().split()))
num.sort()
if n%2 == 1:
     print(num[n//2])
else:
     print(num[(n//2)-1])