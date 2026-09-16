import sys
input = sys.stdin.readline

N=int(input())
house = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0]*N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1
#dp[0][x][y] == 가로 dp[1][x][y] == 대각선 dp[2][x][y] == 세로
for i in range(2,N):
    if house[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for x in range(1,N):
    for y in range(1,N): # 대각선 판정 및 추가 
        if house[x][y] == 0 and house[x][y-1] == 0 and house[x-1][y] == 0:
            dp[1][x][y] = dp[0][x-1][y-1] + dp[1][x-1][y-1] + dp[2][x-1][y-1]
                        # 가로 세로 추가 
        if house[x][y] == 0:
            dp[0][x][y] = dp[0][x][y-1] + dp[1][x][y-1]
            dp[2][x][y] = dp[2][x-1][y] + dp[1][x-1][y]
print(sum((dp[i][N-1][N-1]) for i in range(3)))