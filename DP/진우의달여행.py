import sys
input = sys.stdin.readline

n,m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]
INF = float('inf')

# N X M X 3
# dp[y][x][d] = (y행, x열)에 **d 방향으로 도착**했을 때의 최소 연료 소비량
 
dp = [[[INF] * 3 for _ in range(m)] for _ in range(n)]

for x in range(m):
    for d in range(3):
        dp[0][x][d] = space[0][x]

dx = [-1 , 0 , 1]

for y in range(1,n):
    for x in range(m):
        for d in range(3):
            nx = x + dx[d]
            if 0 <= nx < m:
                for pre in range(3):
                    if d == pre:
                        continue
                    dp[y][x][d] = min(dp[y][x][d] , dp[y-1][nx][pre] + space[y][x])
ans = INF
for x in range(m):
    for d in range(3):
        ans = min(ans , dp[n-1][x][d])
print(ans)