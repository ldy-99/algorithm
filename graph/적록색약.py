import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input().strip())
grid = [list(input().strip()) for _ in range(N)]
move= [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = set()

cnt1 = 0  # 일반인
cnt2 = 0  # 적록색 
def dfs(x,y):
    visited.add((x,y))
    for nx,ny in move:
        dx,dy = x+nx , y+ny
        if 0 <= dx < N and 0<= dy < N and (dx ,dy) not in visited:
            if grid[dx][dy] == c:
                dfs(dx,dy)
                
for c in ['R','G','B']:
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited and grid[i][j] == c:
                dfs(i,j)
                cnt1 += 1  # 일반인 개수 증가
                
for i in range(N):
    for j in range(N):
        if grid[i][j] == "G":
            grid[i][j] = "R"
visited = set()
for c in ['R','B']:
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited and grid[i][j] ==c:
                dfs(i,j)
                cnt2 +=1  # 적록색 개수 증가 
print(cnt1, cnt2)