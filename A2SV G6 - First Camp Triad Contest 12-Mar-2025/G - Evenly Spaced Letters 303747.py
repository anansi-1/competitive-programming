# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

t = int(input())

for _ in range(t):
    s = sorted(input())
    print("".join(s))