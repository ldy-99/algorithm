import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
grid = [list(input().strip()) for _ in range(N)]

start = None
target = None
for r in range(N):
    for c in range(M):
        if grid[r][c] == 'C':
            start = (r,c)
        elif grid[r][c] == 'D':
            target = (r,c)

def fall(r,c,dir):
    while True:
        if 0 <= r < N and grid[r][c] == 'D':
            return r,c,True
        nxt_r = r + (1 if dir == 0 else -1)
        if nxt_r < 0 or nxt_r >= N:
            # 바깥으로 떨어지면 유효한 위치가 없다고 판단
            return None,None,False
        if grid[nxt_r][c] == '#':
            # 다음 칸에 벽이 있으면 현재 위치에 멈춤
            return r,c,False
        r = nxt_r
    return None,None,False

INF = float('inf')
dist = [[[INF] * 2 for _ in range(M)] for _ in range(N)]
q = deque()

sr,sc = start
fr,fc,reached = fall(sr,sc,0)

if reached:
    print(0)
    sys.exit(0)

# 0은 아래방향 1은 위
if fr is not None:
    dist[fr][fc][0] = 0
    q.append((fr,fc,0))
    
    while q:
        r,c,dir = q.popleft()
        for d in [-1,1]:
            nc = c + d
            if 0 <= nc < M and grid[r][nc] != '#':
                fr,fc,reached = fall(r,nc,dir)
                if reached:
                    # 좌우 이동 후 곧바로 D에 닿는다면 현재 상태의 비용이 정답
                    print(dist[r][c][dir])
                    sys.exit(0)
                if fr is not None and dist[fr][fc][dir] > dist[r][c][dir]:
                    dist[fr][fc][dir] = dist[r][c][dir]
                    q.appendleft((fr,fc,dir)) # 좌우 이동은 비용 없음
        new_dir = 1 - dir
        fr,fc,reached = fall(r,c,new_dir)
        if reached:
            print(dist[r][c][dir] + 1)
            sys.exit(0)
        if fr is not None and dist[fr][fc][new_dir] > dist[r][c][dir] + 1 :
            dist[fr][fc][new_dir] = dist[r][c][dir] + 1
            q.append((fr,fc,new_dir))
    print(-1)
else:
    print(-1)