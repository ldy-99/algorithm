# 백준 점프점프 11060
# 이동 규칙: i번째 칸에 적힌 수 A_{i} 이하만큼 오른쪽으로 점프 가능 (예: 값이 3이면 1, 2, 3칸 점프 가능).
import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

dp = [float('inf')] * N
dp[0] = 0

for i in range(N):
    for j in range(1 , A[i] + 1):
        if i+j < N:
            dp[i+j] = min(dp[i+j] , dp[i] + 1)

print(dp[N-1] if dp[N-1] != float('inf') else -1)