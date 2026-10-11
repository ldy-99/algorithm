# 풍선 터트리기(프로그래머스)
# 시뮬레이션이나 각 풍선마다 좌우를 검사하면 시간 초과
# 전체 구간에서 최솟값을 기준으로 잡고 양쪽에서 최솟값 갱신 횟수를 카운트하면 O(N) 에 가능하다.
def solution(a):
    min_idx = a.index(min(a))
    answer = 0

    left_min = float('inf')
    for i in range(min_idx + 1):
        if a[i] < left_min:
            left_min = a[i]  # 왼쪽 최솟값 갱신
            answer += 1

    right_min = float('inf')
    for i in range(len(a) - 1, min_idx - 1, -1):
        if a[i] < right_min:
            right_min = a[i]  # 오른쪽 최솟값 갱신
            answer += 1

    return answer - 1 # 겹치는 카운트 제거