# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

lenn = int(input())
n = input()
s = []
s.append(n[0])
for i in range(1,len(n)):
    if s and s[-1] != n[i]:
        s.pop()
    else:
        s.append(n[i])
print(len(s))