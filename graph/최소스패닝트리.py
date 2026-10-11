# 최소스패닝 트리 대표 유형

import sys
input = sys.stdin.readline

def find(p, x):
    if p[x] == x:
        return x

    p[x] = find(p, p[x])
    return p[x]

def union(p, size, x, y):
    xroot = find(p, x)
    yroot = find(p, y)

    # 이미 같은 집합이면 합칠 필요 없음
    if xroot == yroot:
        return

    # 항상 작은 집합을 큰 집합 밑에 붙임
    if size[xroot] < size[yroot]:
        xroot, yroot = yroot, xroot

    p[yroot] = xroot
    size[xroot] += size[yroot]


n, m = map(int, input().split())

p = [i for i in range(n + 1)]
size = [1] * (n + 1)

edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

ans = 0
lines = 0
max_edge = 0

for cost, a, b in edges:
    if find(p, a) != find(p, b):
        union(p, size, a, b)

        ans += cost
        max_edge = max(max_edge, cost)
        lines += 1

    if lines == n - 1:
        break

print(ans - max_edge)