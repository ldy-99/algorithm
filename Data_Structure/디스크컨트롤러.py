import heapq as hq
from collections import deque

# 우선순위
# 작업 소요시간 > 요청 시각 > 작업 번호

def solution(jobs):
    N = len(jobs)
    answer = 0
    time = 0
    wait = []

    # 1. 작업 요청 시각을 기준으로 정렬
    jobs.sort()
    jobs = deque(jobs)

    # 2. 처리하지 않은 작업 또는 대기 작업이 있으면 반복
    while jobs or wait:

        # 3. 현재 시각까지 요청된 작업을 힙에 추가
        while jobs and jobs[0][0] <= time:
            start, duration = jobs.popleft()
            hq.heappush(wait, (duration, start))

        # 4. 실행 가능한 작업이 있다면
        if wait:
            # 소요 시간이 가장 짧은 작업 선택
            duration, start = hq.heappop(wait)

            # 작업 완료 시각 갱신
            time += duration

            # 반환 시간 누적
            answer += time - start

        else:
            # 5. 대기 작업이 없다면 다음 요청 시각으로 이동
            time = jobs[0][0]

    # 6. 평균 반환 시간 반환
    return answer // N