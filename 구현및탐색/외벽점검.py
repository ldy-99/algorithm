# 프로그래머스 외벽점검
# 친구를 몇 명 사용할 것인가?
# 각 친구를 어느 위치에서 출발시킬 것인가?
# 어떤 친구부터 투입할 것인가?
# 원형구조 처리를 어떻게 할 것인가 ?

from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)

    ex = weak + [w + n for w in weak]    # 원형 구조를 수직선으로 표현

    for start, w in enumerate(weak):  # 취약지점과 인덱스
        for d in permutations(dist):  # 친구들의 투입순서 d
            cnt = 1  # 첫번째 친구부터
            end = w + d[0]

            for i in range(start, start + length):
                # 친구가 도달 못할 경우
                if ex[i] > end:
                    cnt += 1
                    # 친구 부족하면 중단
                    if cnt > len(dist):
                        break
                    
                    # 새 친구의 점검
                    end = ex[i] + d[cnt - 1]

            if cnt <= len(dist):
                answer = min(answer, cnt)

    return answer if answer <= len(dist) else -1

# 최종 시간 복잡도 : O(w^2 * d!)