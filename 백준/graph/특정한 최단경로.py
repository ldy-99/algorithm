import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def dijk(start,graph,N):
    INF = float('inf')
    dist = {node : INF for node in range(1,N+1)}
    dist[start] = 0
    pq = [(0,start)]
    
    while pq:
        curdist , curnode = heapq.heappop(pq)
        if curdist > dist[curnode]:
            continue
        
        for next , weight in graph[curnode]:
            new_dist = curdist + weight
            if new_dist < dist[next]:
                dist[next] = new_dist
                heapq.heappush(pq , (new_dist , next))
    return dist

N , E = map(int,input().split())
graph = defaultdict(list)
for _ in range(E):
    u , v , dist = map(int,input().split())
    graph[u].append((v,dist))
    graph[v].append((u,dist))
    
v1 , v2 = map(int,input().split())

dist1 = dijk(1,graph,N)
dist_v1 = dijk(v1,graph,N)
dist_v2 = dijk(v2,graph,N)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[N]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[N]

ans = min(path1 , path2)
print(ans if ans < float('inf') else -1)