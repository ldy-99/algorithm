import sys
input = sys.stdin.readline
from collections import deque

m,n,h = map(int,input().split())
tomato = [[[0] * m for _ in range(n)] for _ in range(h)]
for z in range(h):
    for y in range(n):
        tomato[z][y] = list(map(int,input().split()))

dz = [0,0,0,0,1,-1]
dy = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]

q = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato[z][y][x] == 1:
                q.append((z,y,x))

while q:
    z,y,x = q.popleft()
    for i in range(6):
        nz,ny,nx = z + dz[i] , y + dy[i] , x + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m :
            if tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                q.append((nz,ny,nx))
day = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato[z][y][x] == 0:
                print(-1)
                sys.exit(0)
            day = max(day , tomato[z][y][x])
print(day-1)