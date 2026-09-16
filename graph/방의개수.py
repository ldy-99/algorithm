# 프로그래머스 방의 개수
def solution(arrows):
    
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    x, y = 0, 0
    
    visited_node = {(0, 0)}
    visited_edge = set()
    answer = 0

    for arrow in arrows:
        # 교차점 처리(정수 좌표로 처리)
        for _ in range(2):
            nx = x + dx[arrow]
            ny = y + dy[arrow]

            # 방 판정 알고리즘
            if (nx, ny) in visited_node and ((x, y), (nx, ny)) not in visited_edge:
                answer += 1

            visited_node.add((nx, ny))
            visited_edge.add(((x, y), (nx, ny)))
            visited_edge.add(((nx, ny), (x, y)))
            x, y = nx, ny
    return answer