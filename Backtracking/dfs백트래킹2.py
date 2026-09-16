import sys
input = sys.stdin.readline

def cal(start,link):
    ssum = 0
    lsum = 0
    
    for i in start:
        for j in start:
            ssum += S[i][j]
    
    for i in link:
        for j in link:
            lsum += S[i][j]
    
    return abs(ssum - lsum)

def dfs(depth , start):
    global ans
    if len(start) == N // 2:
        link = [i for i in range(N) if i not in start]
        minus = cal(start,link)
        ans = min(ans , minus)
        return
    
    for i in range(depth , N):
        if i not in start:
            start.append(i)
            dfs(i+1 , start)
            start.pop()

N=int(input())
S=[list(map(int,input().split())) for _ in range(N)]
ans=float('inf')
dfs(0, [])
print(ans)