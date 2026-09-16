import sys
input = sys.stdin.readline

def sol(K,file):
    sum_ = [0] * (K+1)
    for i in range(1,K+1):
        sum_[i] = sum_[i-1] + file[i-1]
    
    DP = [[0] * K for _ in range(K)]
    
    # L개의 파일을 합치는 경우 
    for L in range(2,K+1):
        for i in range(K-L+1):
            j = i + L - 1   # 구간의 시작점 i 일때 끝 점 j 계산 
            DP[i][j] = float('inf')
            
            for k in range(i,j):
                cost = DP[i][k] + DP[k+1][j] + (sum_[j+1] - sum_[i])
                DP[i][j] = min(DP[i][j] , cost)
                
    return DP[0][K-1]

T=int(input())
ans = []

for _ in range(T):
    K = int(input().strip())
    file = list(map(int,input().split()))
    ans.append(str(sol(K,file)))

print("\n".join(ans))