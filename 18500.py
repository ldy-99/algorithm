# 백준 18500 / 그래프 탐색 , 시뮬레이션
import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
grid = [list(input().strip()) for _ in range(R)]
N=int(input())
height = list(map(int,input().split()))

def stick(turn,height):
    '''막대를 던져서 부숨'''
    if turn % 2 == 0 :
        for j in range(C):
            if grid[R-height][j] == 'x' :
                grid[R-height][j] = '.'
                return (R-height,j)
    else:
        for j in range(C-1,-1,-1):
            if grid[R-height][j] == 'x':
                grid[R-height][j] = '.'
                return (R-height,j)

def find_cluster(x,y):
    '''공중에 떠있는 클러스터를 찾는다'''
    is_floating = True
    cluster = []
    visited = set()
    visited.add((x,y))
    q = deque()
    q.append((x,y))
    while q :
        cx,cy = q.popleft()
        cluster.append((cx,cy))
        
        if cx == R-1 :
            is_floating = False

        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 'x' and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.append((nx,ny))
    return cluster if is_floating else False

def fall_cluster(node):
    ''' 떨어지는 거리 계산'''
    for r,c in node :
        grid[r][c] = '.'
    fall_dist = R
    for r,c in node :
        dist = 0
        nr = r
        while True:
            nr += 1
            if nr == R or grid[nr][c] == 'x' :
                break
            dist += 1
        fall_dist = min(fall_dist , dist)
    for r,c in node :
        grid[r + fall_dist][c] = 'x'

for i in range(N):
    broken = stick(i , height[i])
    
    if broken :
        r,c = broken
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)] :
            nr , nc = r + dr , c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 'x':
                floating = find_cluster(nr,nc)
                if floating:
                    fall_cluster(floating)
                    break
for row in grid:
    print("".join(row))