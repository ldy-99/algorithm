import sys
input = sys.stdin.readline
from collections import deque

def solve(w,h,maps) :
    fire_dist = [[-1] * w for _ in range(h)]
    dist = [[-1] * w for _ in range(h)]
    fire_q = deque()
    person_q = deque()
    
    for i in range(h) :
        for j in range(w) :
            if maps[i][j] == 'F' :
                fire_q.append((i,j))
                fire_dist[i][j] = 0
            elif maps[i][j] == 'J' :
                person_q.append((i,j))
                dist[i][j] = 0
                
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    while fire_q :
        x,y = fire_q.popleft()
        for i in range(4):
            nx , ny = x + dx[i] , y + dy[i]
            if 0 <= nx < h and 0 <= ny < w :
                if maps[nx][ny] != '#' and fire_dist[nx][ny] == -1 :
                    fire_dist[nx][ny] = fire_dist[x][y] + 1
                    fire_q.append((nx,ny)) 
                           
    while person_q :
        x,y = person_q.popleft()
        # 맵 바깥으로 나가야 탈출을 한다 이걸 써보면
        if x == 0 or x == h-1 or y == 0 or y == w-1 :
            return dist[x][y] + 1
        for i in range(4) :
            nx,ny = x + dx[i] , y + dy[i]
            if 0 <= nx < h and 0 <= ny < w :
                if maps[nx][ny] == '#' or dist[nx][ny] != -1 :
                    continue
                if fire_dist[nx][ny] == -1 or fire_dist[nx][ny] > dist[x][y] + 1 :
                    dist[nx][ny] = dist[x][y] + 1
                    person_q.append((nx,ny))
                    
    return "IMPOSSIBLE"

h , w = map(int,input().split())
maps = [list(input().strip()) for _ in range(h)]
print(solve(w,h,maps))