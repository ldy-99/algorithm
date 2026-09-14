import sys
from collections import deque
input = sys.stdin.readline

N , L , R = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
move= [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(x,y):
    q = deque([(x,y)])
    union = [(x,y)]
    
    while q:
        a , b = q.popleft()
        for dx , dy in move:
            nx , ny = a + dx , b + dy
            if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in visited:
                if L <= abs(grid[a][b] - grid[nx][ny]) <= R:
                    visited.add((nx,ny))
                    q.append((nx,ny))
                    union.append((nx,ny))
    if len(union) <= 1:
        return 0
    ans = sum(grid[a][b] for a,b in union) // len(union)
    for a ,b in union:
        grid[a][b] = ans
    return 1

days = 0
while True:
    cnt = 0  # 오늘 연합이 형성된 횟수 
    visited = set() # 오늘 방문한 좌표 저장 
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited:
                visited.add((i,j))
                cnt += bfs(i,j) # 오늘 연합이 있었는지 체크 
    if cnt == 0: # 연합이 한번도 형성되지 않아야 인구이동 끝 
        break
    days +=1
print(days)