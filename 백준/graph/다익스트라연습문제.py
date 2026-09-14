#백준 1800번 인터넷 설치
import sys
import heapq
input = sys.stdin.readline

def dijk(X):
    INF = 10**9
    dist = [INF] * (N + 1)
    dist[1] = 0

    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for nxt, cost in graph[u]:
            nd = d + (1 if cost > X else 0)
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

    return dist[N] <= K

N, P, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_cost = 0

for _ in range(P):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_cost = max(max_cost, c)

left, right = 0 , max_cost
ans = -1

while left <= right:
    mid = (left + right) // 2
    if dijk(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)