import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
# k+1 , K+1+2 , k+1+2+3
# 1초후 n+1,n-1,2n
MAX = 500000
def bfs(n):
    visited = [[-1] * 2 for _ in range(MAX+1)]
    # visited[x][0] = 짝수 시간에 x에 도달 가능한 최소 시간
    # visited[x][1] = 홀수 시간에 x에 도달 가능한 최소 시간

    q = deque([(n,0)])
    visited[n][0] = 0  #  visited[5][0]
    
    while q :
        cur ,t = q.popleft()
        
        for nxt in (cur-1 , cur+ 1 , 2*cur) : # 4,6,10  , t =0
            if 0 <= nxt <= MAX and visited[nxt][(t+1)%2] == -1 : # 다음 도착 t+1
                visited[nxt][(t+1)%2] = t+1   # visited[4][1] = 1
                q.append((nxt,t+1))
    return visited

def solve(n,k):
    visited = bfs(n)
    t = 0
    while 1:
        pos = k + t * (t+1) // 2  # 동생위치 계산 17
        if pos > MAX : return -1
        if visited[pos][t%2] != -1 and visited[pos][t%2] <= t :  # 수빈 방문 검증
            return t     #visited[20][0] = 2 <= 2
        t+= 1
print(solve(N,K))