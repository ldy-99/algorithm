import sys
input = sys.stdin.readline

N = int(input())
height = [int(input()) for _ in range(N)]
stack = []  # (height , count)
ans = 0

for h in height : 
    cnt = 1
    
    while stack and stack[-1][0] <= h:
        top_h , top_cnt = stack.pop()
        ans += top_cnt
        if top_h == h :
            cnt += top_cnt
            
    if stack:
        ans += 1
    stack.append((h,cnt))
print(ans)