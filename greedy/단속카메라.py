# 프로그래머스 단속 카메라
# 차량들의 구간을 모두 단속하기 위한 최소 카메라의 개수
# 진출지점(끝점) 을 기준으로 선택하는게 왜 그리디적으로 안전한가
# 처리 할 수 없는 구간이 등장했을 때 새로운 카메라를 설치한다
def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 0
    camera = float('-inf')

    for start, end in routes:
        if start > camera:
            camera = end
            answer += 1

    return answer