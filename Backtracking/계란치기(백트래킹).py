import sys
input=  sys.stdin.readline

N= int(input())
egg = [list(map(int,input().split())) for _ in range(N)]
ans = 0

def dfs(idx):
    global ans
    
    if idx == N :
        broken = sum(1 for s,_ in egg if s<=0)
        ans = max(ans , broken)
        return
    
    if egg[idx][0] <= 0 :
        dfs(idx + 1)
        return
    
    target = False
    for i in range(N):
        if i == idx or egg[i][0] <= 0:
            continue
        target = True
        egg[idx][0] -= egg[i][1]
        egg[i][0] -= egg[idx][1]
        
        dfs(idx +1)
        
        egg[idx][0] += egg[i][1]
        egg[i][0] += egg[idx][1]
        
    if not target:
        dfs(idx + 1)
dfs(0)
print(ans)