import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
grid = []
coins = []

def out(x,y,n,m):
    return not (0 <= x < n and 0 <= y < m)

def bfs(grid,n,m,coins):
    visited = set()
    (x1,y1) , (x2,y2) = coins
    q = deque([(x1,y1,x2,y2,0)])
    visited.add((x1,y1,x2,y2))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q:
        x1,y1,x2,y2,cnt = q.popleft()
        if cnt >= 10:
            break
        
        for d in range(4):
            nx1 , ny1 = x1 + dx[d] , y1 + dy[d]
            nx2 , ny2 = x2 + dx[d] , y2 + dy[d]
            
            if not out(nx1 , ny1 , n ,m) and grid[nx1][ny1] == '#':
                nx1 , ny1 = x1 , y1
            if not out(nx2 , ny2 , n, m) and grid[nx2][ny2] == '#':
                nx2 , ny2 = x2 , y2
            
            out1 = out(nx1,ny1,n,m)
            out2 = out(nx2,ny2,n,m)
            
            if out1 and out2:
                continue
            if out1 or out2:
                return cnt + 1
            
            state = (nx1 , ny1 , nx2 , ny2)
            if state not in visited:
                visited.add(state)
                q.append((nx1,ny1,nx2,ny2, cnt+1))
    return -1

for i in range(N):
    row = list(input())
    for j in range(M):
        if row[j] == 'o':
            coins.append((i,j))
            row[j] == '.'
    grid.append(row)
print(bfs(grid,N,M,coins))