import sys
input = sys.stdin.readline

N,M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r,c))
        elif city[r][c] == 2:
            chickens.append((r,c))
            
ans = float('inf')

# 최대 M개의 치킨집 , 도시의 치킨거리는 최소가 되게

def dist(houses,chicken):
    total = 0
    
    for hx,hy in houses:
        min_dist = float('inf')
        
        for cx,cy in chicken:
            min_dist = min(min_dist , abs(hx-cx) + abs(hy-cy))
        total += min_dist
    return total

def dfs(depth , arr):
    global ans
    
    if len(arr) == M :
        city_dist = dist(houses,arr)
        ans = min(ans, city_dist)
        return
    
    for d in range(depth, len(chickens)):
        arr.append(chickens[d])
        dfs(d+1 , arr)
        arr.pop()

dfs(0 , [])
print(ans)