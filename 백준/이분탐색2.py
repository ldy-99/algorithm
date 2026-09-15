import sys
input = sys.stdin.readline

n,m=map(int,input().split())
title = [input().split() for _ in range(n)]
strong = [int(input().strip()) for _ in range(m)]

for s in strong:
    left , right = 0 , n-1
    ans = 0
    while left <= right:
        mid = (left + right ) //2
        if int(title[mid][1]) >= s:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(title[ans][0])