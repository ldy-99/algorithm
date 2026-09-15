import sys
input = sys.stdin.readline

def solution(board):
    
    def is_valid(num, row, col):
        return not (in_row(num, row) or in_col(num, col) or in_box(num, row, col))

    def in_row(num, row):
        return num in board[row]

    def in_col(num, col):
        return num in (board[i][col] for i in range(9))

    def in_box(num, row, col):
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return True
        return False

    def is_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def dfs():
        empty = is_empty()
        if not empty:
            return True
        r, c = empty
        for num in range(1, 10):
            if is_valid(num, r, c):
                board[r][c] = num
                if dfs():
                    return True
                board[r][c] = 0
        return False
    dfs()
    return board

board = [list(map(int, input().strip())) for _ in range(9)]

ans = solution(board)
for row in ans:
    print("".join(map(str,row)))