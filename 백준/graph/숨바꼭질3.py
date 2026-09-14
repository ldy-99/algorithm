import sys
input = sys.stdin.readline
import heapq

def dijk(start,end):
    INF = float("inf")
    dist = {node : INF for node in range(100001)}
    dist[start] = 0
    pq = [(0,start)]
    
    while pq:
        curdist,curnode = heapq.heappop(pq)
        if curdist > dist[curnode]:
            continue
        
        for next in (curnode+1 , curnode-1 , curnode*2):
            if next < 0 or next > 100000:
                continue
            new_dist = curdist
            
            if next != curnode *2:
                new_dist = curdist + 1
            
            if new_dist < dist[next]:
                dist[next] = new_dist
                heapq.heappush(pq,(new_dist,next))
    return dist[end]

N, K = map(int, input().split())
print(dijk(N,K))