# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

t = int(input())
value = {"S": 0, "M": 1, "L": 2}
for _ in range(t):
    a, b = input().split()
    if a == b:
        print("=")
    else:
        if a[-1] == b[-1]:  
            c_a = a.count("X")
            c_b = b.count("X")
            if c_a > c_b:
                print(">" if a[-1] == "L" else "<")
            else:
                print("<" if a[-1] == "L" else ">")
        else:
            if value[a[-1]] > value[b[-1]]:
                print(">")
            else:
                print("<")