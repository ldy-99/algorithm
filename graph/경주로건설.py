# 프로그래머스 경주로건설
# 초기 방향을 어떻게 설정하냐가 중요한 것 같음.
# 3차원의 상태 저장및 관리 연습

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

import heapq

def solution(board):  
    N = len(board)
    INF = float('inf')
    cost = [[[INF] * 4 for _ in range(N)] for _ in range(N)] # cost[y][x][d]
    pq = []
    heapq.heappush(pq ,(0,0,0,-1))
    
    while pq :
        cur_cost , y , x , prev_dir = heapq.heappop(pq)
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            
            if not (0 <= nx < N and 0 <= ny < N) :
                continue
            
            if board[ny][nx] == 1 :
                continue
            
            if prev_dir == -1 or prev_dir == d :
                new_cost = cur_cost + 100
            else:
                new_cost = cur_cost + 600
            
            if new_cost < cost[ny][nx][d]:
                cost[ny][nx][d] = new_cost
                heapq.heappush(pq, (new_cost, ny, nx, d))

    return min(cost[N-1][N-1])