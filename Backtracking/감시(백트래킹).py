import sys
import copy
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

cctvs = []
for i in range(n):
    for j in range(m):
        if 1<=board[i][j]<=5:
            cctvs.append((i,j,board[i][j]))

direction = {
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[3,0]],
    4: [[0,1,3],[0,1,2],[1,2,3],[0,2,3]],
    5: [[0,1,2,3]]
}

def solution(x,y,dir,board):  # cctv 의 감시영역 
    for d in dir:
        nx , ny = x,y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < n and 0 <= ny < m): break
            if board[nx][ny] == 6 : break
            if board[nx][ny] == 0:
                board[nx][ny] = '#'

def count0(board):
    return sum(row.count(0) for row in board)

def backtrack(idx,board):
    global mins
    if idx == len(cctvs):
        mins = min(mins , count0(board))
        return
    
    x,y,types = cctvs[idx]
    for dir in direction[types]:
        temp = copy.deepcopy(board)
        solution(x,y,dir,temp)
        backtrack(idx+1 , temp)

mins = n * m
backtrack(0,board)
print(mins)