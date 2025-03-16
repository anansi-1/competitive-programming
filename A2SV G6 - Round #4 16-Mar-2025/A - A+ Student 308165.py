# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

testcases = int(input())
for _ in range((testcases)):
    a,b,c = map(int,input().split())
    f = max(0,max(b,c)-a+1)
    s =max(0,max(a,c)-b + 1)
    t = max(0,max(a,b)-c + 1)
    print(f,s,t)