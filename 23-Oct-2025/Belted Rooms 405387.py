# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

for _ in range(int(input())):
    n = int(input())
    s = input()
    f, se = 0, 0
    for i in s:
        if i == ">":
            f += 1
        elif i == "<":
            se += 1
    if f == 0 or se == 0:
        print(n)
    else:
        c = 0
        for i in range(n):
            if s[i] == "-":
                if s[i - 1] == ">" or s[i - 1] == "<":
                    c += 2
                else:
                    c += 1
        print(c)