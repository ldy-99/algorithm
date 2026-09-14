import sys
import copy
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

def left(board):
    for i in range(N):
        cur = 0
        for j in range(1,N):
            if board[i][j] != 0 :
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[i][cur] == 0 :
                    board[i][cur] = tmp
                    
                elif board[i][cur] == tmp :
                    board[i][cur] *= 2
                    cur += 1
                else:
                    cur += 1
                    board[i][cur] = tmp
    return board

def right(board):
    for i in range(N):
        cur = N-1
        for j in range(N-1,-1,-1):
            if board[i][j] != 0 :
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[i][cur] == 0 :
                    board[i][cur] = tmp
                    
                elif board[i][cur] == tmp :
                    board[i][cur] *= 2
                    cur -= 1
                else:
                    cur -= 1
                    board[i][cur] = tmp
    return board

def up(board):
    for j in range(N):
        cur = 0
        for i in range(N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cur][j] == 0:
                    board[cur][j] = tmp

                elif board[cur][j] == tmp:
                    board[cur][j] *= 2
                    cur += 1

                else:
                    cur += 1
                    board[cur][j] = tmp
    return board

def down(board):
    for j in range(N):
        cur = N - 1
        for i in range(N - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cur][j] == 0:
                    board[cur][j] = tmp

                elif board[cur][j] == tmp:
                    board[cur][j] *= 2
                    cur -= 1
                else:
                    cur -= 1
                    board[cur][j] = tmp
    return board

ans = 0
def dfs(depth, arr):
    global ans
    if depth == 5 :
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans :
                    ans = arr[i][j]
        return
    for i in range(4):
        new_board = copy.deepcopy(arr)
        if i == 0 :
            dfs(depth+1 , left(new_board))
        elif i == 1 :
            dfs(depth+1 , right(new_board))
        elif i == 2:
            dfs(depth+1 , up(new_board))
        else:
            dfs(depth+1 , down(new_board))
dfs(0,board)
print(ans)