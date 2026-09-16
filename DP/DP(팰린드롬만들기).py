import sys
input = sys.stdin.readline

def sol(arr):
    dp = [[0]* N for _ in range(N)]
    for length in range(2,N+1): # 부분 수열 길이
        for i in range(N -length +1): # 시작
            j = i + length - 1  # 끝
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j],dp[i][j-1]) + 1
    return dp[0][N-1]

N = int(input())
arr = list(map(int,input().split()))
print(sol(arr))