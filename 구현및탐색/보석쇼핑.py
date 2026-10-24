#프로그래머스 보석 쇼핑 (투 포인터 , 슬라이딩 윈도우)

from collections import defaultdict

def solution(gems):
    total = len(set(gems))

    left = 0
    count = defaultdict(int)
    min_length = float('inf')
    answer = []

    for right in range(len(gems)):

        # 오른쪽 포인터의 보석 추가
        count[gems[right]] += 1

        # 모든 종류의 보석이 포함되어 있다면
        while len(count) == total:

            # 현재 구간 길이 계산
            length = right - left + 1

            # 최소 길이 갱신
            if length < min_length:
                min_length = length
                answer = [left + 1, right + 1]

            # 왼쪽 포인터의 보석 제거
            count[gems[left]] -= 1

            # 보석 개수가 0이면 딕셔너리에서 삭제
            if count[gems[left]] == 0:
                del count[gems[left]]

            # 왼쪽 포인터 이동
            left += 1
    return answer