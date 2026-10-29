# 프로그래머스 N으로 표현
# N과 사칙연산만으로 number 을 표현할 수 있는 사용횟수의 최솟값을 구하기.
# N으로 표현 문제에서는 N을 i번 사용하여 여러 숫자를 만들 수 있어.
# 따라서 하나의 숫자가 아니라 여러 결과를 저장할 자료구조가 필요해.
def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        # N을 i번 이어 붙인 숫자 (사칙연산 사용하지 않은 경우)
        dp[i].add(int(str(N) * i))

        # N 사용 횟수를 두 부분으로 나누기
        for j in range(1, i):

            # 이전에 계산한 집합들을 조합
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)

                    if b != 0:
                        dp[i].add(int(a / b))
        # 목표 숫자를 만들었다면 최소 사용 횟수 반환
        if number in dp[i]:
            return i

    return -1