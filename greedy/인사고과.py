# 프로그래머스 인사고과
# 정렬 , 그리디
def calc(arr):
    return arr[0] + arr[1]

def solution(scores):
    # 처음엔 1등으로 시작
    answer = 1
    wanho = scores[0]
    wanho_total = calc(wanho)
    
    # 정렬(중요)
    # 두개의 지표를 비교하기 위한 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))
    max_second = 0
    for a, b in scores:
        # 인센티브 대상 제외
        if b < max_second:
            # 완호가 제외되는 경우
            if [a, b] == wanho:
                return -1
            continue
        # 두 번째 점수의 최댓값 갱신
        max_second = b
        # 완호보다 점수의 합이 높은 경우
        if a + b > wanho_total:
            answer += 1
    return answer