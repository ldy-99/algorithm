import sys
input = sys.stdin.readline
from collections import defaultdict, deque
import heapq

INF = float("inf")

def dijkstra(N, graph, start):
    dist = [INF] * (N + 1)
    pre = [[] for _ in range(N + 1)]

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        curdist, u = heapq.heappop(pq)
        if curdist > dist[u]:
            continue

        for v, w in graph[u]:
            nd = curdist + w
            if nd < dist[v]:
                dist[v] = nd
                pre[v] = [u]
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                pre[v].append(u)

    return dist, pre

def bfs(pre, start, blocked):
    q = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True

    while q:
        v = q.popleft()
        for u in pre[v]:
            if not blocked[u][v]:
                blocked[u][v] = True
                if not visited[u]:
                    visited[u] = True
                    q.append(u)

def dijkstra2(N, graph, start, blocked):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        curdist, u = heapq.heappop(pq)
        if curdist > dist[u]:
            continue

        for v, w in graph[u]:
            if blocked[u][v]:
                continue
            nd = curdist + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    A, B = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))

    dist, pre = dijkstra(N, graph, A)

    if dist[B] == INF:
        print(-1)
        continue
    
    blocked = [[False] * (N + 1) for _ in range(N + 1)]
    bfs(pre, B, blocked)
    dist2 = dijkstra2(N, graph, A, blocked)
    print(dist2[B] if dist2[B] != INF else -1)