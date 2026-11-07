# 프로그래머스 스티커 모으기
# 원형구조임에 주목
# dp 배열을 나눠서 생각
def solution(sticker):
    N = len(sticker)
    # 스티커가 하나라면 해당 스티커 선택
    if N == 1:
        return sticker[0]

    # 경우 1: 첫 번째 스티커 선택
    dp1 = [0] * N
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]

    for i in range(2, N-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])

    # 경우 2: 첫 번째 스티커 선택하지 않음
    dp2 = [0] * N
    dp2[1] = sticker[1]

    for i in range(2, N):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])

    return max(dp1[N-2], dp2[N-1])