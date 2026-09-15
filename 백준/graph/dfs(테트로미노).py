import sys
input = sys.stdin.readline

move= [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0
visited = set()

def dfs(x,y,depth,total):
    global ans
    if depth == 4:
        ans = max(ans , total)
        return
    for nx,ny in move:
        dx , dy = x + nx, y + ny
        if 0<= dx < N and 0<= dy < M and (dx,dy) not in visited:
            visited.add((dx,dy))
            dfs(dx,dy,depth + 1 , total + grid[dx][dy])
            visited.remove((dx,dy))
#  ㅗ 모양만 따로 검사            
def checkFuck(x,y):
    global ans
    for i in range(4):
        total = grid[x][y]
        cnt = 0
        for j in range(4):
            if i==j:
                continue
            dx = x + move[j][0]
            dy = y + move[j][1]

            if 0 <= dx < N and 0 <= dy < M and (dx, dy) not in visited:
                total += grid[dx][dy]
                cnt += 1
        if cnt == 3:
            ans = max(ans, total)
                                 
N , M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

# 모든점에서 dfs 시작  + check 
for i in range(N):
    for j in range(M):
        visited.add((i,j))
        dfs(i,j,1,grid[i][j])
        visited.remove((i,j))
        checkFuck(i,j)
print(ans)