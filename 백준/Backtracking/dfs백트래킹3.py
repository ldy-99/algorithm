import sys
input = sys.stdin.readline

def dfs(arr):
    if len(arr) == M:
        print(*arr)
        return

    prev = -1
    for i in range(N):
        if not visited[i] and prev != numbers[i]:
            visited[i] = 1
            dfs(arr + [numbers[i]])
            visited[i] = 0
            prev = numbers[i]

N, M = map(int,input().split())
numbers = sorted(map(int, input().split()))

visited = [0] * N
dfs([])