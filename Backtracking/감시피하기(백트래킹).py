import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
grid = [list(input().split()) for _ in range(N)]

Teacher = []
empty = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'T':
            Teacher.append((i,j))
        elif grid[i][j] == 'X':
            empty.append((i,j))

def detected():
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    for x, y in Teacher:
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            while 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] == 'O':  
                    break
                if grid[nx][ny] == 'S':
                    return True
                nx += dx
                ny += dy

    return False

for walls in combinations(empty, r=3):
    for x, y in walls:
        grid[x][y] = 'O'

    if not detected():
        print("YES")
        break
    for x, y in walls:
        grid[x][y] = 'X'
else:
    print("NO")