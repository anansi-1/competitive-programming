# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t = map(int,input().split())
arr = list(map(int,input().split()))
max_book = float('-inf')
book_num = 0
curr_time = 0
l = 0
for r in range(len(arr)):
    book_num += 1
    curr_time += arr[r]
    while curr_time > t:
        curr_time -= arr[l]
        l +=1
        book_num -=1
    max_book = max(max_book,book_num)
print(max_book)