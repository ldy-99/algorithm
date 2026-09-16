import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq

def dijk(N,graph,start,end):
    INF = float("inf")
    dist = {node : INF for node in range(1,N+1)}
    pre = {node : None for node in range(1,N+1)}
    dist[start] = 0
    pq = [(0,start)]
    
    while pq:
        curdist,curnode = heapq.heappop(pq)
        if curdist > dist[curnode]: 
            continue
        
        for (nextnode , weight) in graph[curnode]:
            new_dist = curdist + weight
            if new_dist < dist[nextnode]:
                dist[nextnode] = new_dist
                pre[nextnode] = curnode
                heapq.heappush(pq,(new_dist,nextnode))
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = pre[node]
    path.reverse()
    
    return dist[end] , path

N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    u,v,dist = map(int,input().split())
    graph[u].append((v,dist))
start,end = map(int,input().split())
a,b = dijk(N,graph,start,end)
print(a)
print(len(b))
print(*b)