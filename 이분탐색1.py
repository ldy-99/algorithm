import sys
input = sys.stdin.readline

N = int(input())
computers = [list(map(int,input().split())) for _ in range(N)]
total_computer = sum(sum(row) for row in computers)
half = (total_computer + 1) // 2

# 최소 시간이 곧 최소 높이이다 . 
left , right = 0 , max(max(row) for row in computers)
ans = right

while left <= right:
    mid = (left + right) // 2
    
    working = 0
    for i in range(N):
        for j in range(N):
            working += min(mid , computers[i][j])

    if working >= half:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)