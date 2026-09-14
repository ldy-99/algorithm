import sys
input = sys.stdin.readline

R,C,N = map(int,input().split())
grid = [list(input().strip()) for _ in range(R)]

def solution(grid):
    new_grid = [['O'] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j]== 'O':
                new_grid[i][j]='.'
                
                if i> 0 : new_grid[i-1][j] = '.'
                if i < R-1 : new_grid[i+1][j]= '.'
                if j>0 : new_grid[i][j-1] = '.'
                if j < C-1 : new_grid[i][j+1] = '.'
    return new_grid

if N == 1:
    ans = grid
elif N % 4 == 2 or N % 4 == 0:
    ans = [['O']* C for _ in range(R)]
elif N% 4 == 3:
    ans = solution(grid)
else:
    first = solution(grid)
    ans = solution(first)

for row in ans:
    print(''.join(row))