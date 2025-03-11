# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n = int(input())
s = input()
curr = 0
ans = []
ans.append(s[0])
for i in range(1,len(s)):
    curr += i    
    if curr >= len(s):
        break
    ans.append(s[curr])
print("".join(ans))