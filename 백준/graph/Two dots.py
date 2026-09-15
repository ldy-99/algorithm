import sys

# 재귀 DFS 깊이 제한 증가
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# n: 행의 개수, m: 열의 개수
n, m = map(int, input().split())

# 게임판 입력
grid = [list(input().strip()) for _ in range(n)]

# 방문 여부 확인 배열
visited = [[False] * m for _ in range(n)]

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, px, py, color):
    # 현재 위치 방문 처리
    visited[x][y] = True

    # 상하좌우 확인
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 범위 안에 있고, 현재 색과 같은 색인 경우
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == color:

            # 아직 방문하지 않은 칸이라면 계속 DFS 진행
            if not visited[nx][ny]:

                # 현재 위치 (x, y)를
                # 다음 DFS의 이전 위치(px, py)로 넘김
                if dfs(nx, ny, x, y, color):
                    return True

            # 이미 방문한 같은 색 칸을 만난 경우
            else:
                # 그 칸이 바로 직전에 왔던 부모 칸이 아니라면
                # 다른 경로를 통해 다시 만난 것이므로 사이클 존재
                if (nx, ny) != (px, py):
                    return True

    # 끝까지 사이클을 발견하지 못함
    return False


# 모든 칸 확인
for i in range(n):
    for j in range(m):

        # 아직 방문하지 않은 칸에서 DFS 시작
        if not visited[i][j]:

            # 처음에는 이전 위치가 없으므로 (-1, -1)
            # 현재 칸의 색을 기준으로 같은 색만 탐색
            if dfs(i, j, -1, -1, grid[i][j]):
                print("Yes")
                sys.exit()

# 모든 칸을 확인했는데 사이클이 없는 경우
print("No")