# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

n,s = map(int,input().split())
count = 0
if n >= s:
    print(1)
else:
    count = (s+n -1)//n
    print(count)
