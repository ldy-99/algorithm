#플로이드 워셜 기본

import sys
from collections import defaultdict

INF = float('inf')
# 입력 처리
n = int(sys.stdin.readline())  # 정점 개수
graph = defaultdict(list)  # 인접 리스트

m = int(sys.stdin.readline())  # 간선 개수
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))  # 방향 그래프

# 최단 거리 배열 초기화
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0  # 자기 자신 거리 0

# 초기 간선 정보 반영
for u in range(n):
    for v, w in graph[u]:  # u에서 v로 가는 거리 w
        dist[u][v] = w

# 플로이드-워셜 실행
for k in range(n):  # 경유 노드
    for i in range(n):  # 출발 노드
        for j in range(n):  # 도착 노드
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 결과 출력
for row in dist:
    print(*row)