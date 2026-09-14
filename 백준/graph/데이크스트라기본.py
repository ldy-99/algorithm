import heapq
import sys
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(N, D, shortcuts):
    dist = [float('inf')] * (D + 1)
    dist[0] = 0 
    graph = defaultdict(list)
    
    for i in range(D):
        graph[i].append((i + 1, 1))  # 인접 정점의 거리는 1
    for start, end, length in shortcuts:
        if end <= D:
            graph[start].append((end, length))
    pq = [(0, 0)]  # (거리, 노드)
    
    while pq:
        curdist, curnode = heapq.heappop(pq)
        if curdist > dist[curnode]:
            continue  
        for neighbor, weight in graph[curnode]:
            new_dist = curdist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist[D]

N, D = map(int, input().split())
shortcuts = [tuple(map(int, input().split())) for _ in range(N)]
print(dijkstra(N, D, shortcuts))