# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

num = int(input())
ans = []
for i in range(1,num+1):
    ans.append(i)
strr = "".join(map(str,ans))
print(strr[num-1])