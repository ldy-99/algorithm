import sys
input = sys.stdin.readline
from collections import deque

R,C = map(int,input().strip().split())
maps = [list(input().strip()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

wq = deque()
hq = deque()
visited = set()
water = set()

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'S':
            hq.append((i,j,0))
            visited.add((i,j))
        elif maps[i][j] == '*' :
            wq.append((i,j))

def water_bfs():
    for _ in range(len(wq)):   ## while 을쓰게되면 물을 다 퍼트린 다음 고슴도치가 이동하게 됨.
        x,y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0<= ny < C :
               if maps[nx][ny] == '.' and (nx,ny) not in water:
                    water.add((nx,ny))
                    maps[nx][ny] = '*'
                    wq.append((nx,ny))

def hog_bfs():
    while hq:
        water_bfs()
        for _ in range(len(hq)):
            x,y,time = hq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C :
                    if (nx,ny) not in visited :
                        if maps[nx][ny] == 'D' :
                            print(time + 1)
                            return
                        if maps[nx][ny] == '.' :
                            visited.add((nx,ny))
                            hq.append((nx,ny,time+1))
    print("KAKTUS")
hog_bfs()