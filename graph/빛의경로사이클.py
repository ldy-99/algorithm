# 프로그래머스 빛의 경로 사이클
# 단순한 dfs bfs의 사고의 틀을 깨는 문제
# 좌표와 방향까지 함께 생각한 3차원의 상태

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def cycle(y, x, d, grid, visited):
    R, C = len(grid), len(grid[0])
    length = 0

    while not visited[y][x][d]:
        # 현재 좌표와 진행 방향을 방문 처리
        visited[y][x][d] = True
        length += 1

        # 현재 방향으로 이동 (격자 밖으로 나가면 반대편으로 이동)
        y = (y + dy[d]) % R
        x = (x + dx[d]) % C

        # 도착한 칸에서 방향 전환
        if grid[y][x] == 'L':
            d = (d - 1) % 4
        elif grid[y][x] == 'R':
            d = (d + 1) % 4

    return length

def solution(grid):
    R, C = len(grid), len(grid[0])

    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]
    answer = []

    # 모든 좌표에서 4가지 방향을 시작점으로 검사
    for y in range(R):
        for x in range(C):
            for d in range(4):

                if not visited[y][x][d]:
                    length = cycle(y, x, d, grid, visited)
                    answer.append(length)

    return sorted(answer)