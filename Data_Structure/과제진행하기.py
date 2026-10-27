def solution(plans):
    answer = []

    plans.sort(key=lambda x: x[1])
    stack = []
    N = len(plans)

    for i in range(N - 1):
        name, start, playtime = plans[i]
        nxt = plans[i + 1][1]

        HH, MM = map(int, start.split(':'))
        HH2, MM2 = map(int, nxt.split(':'))

        t1 = HH * 60 + MM
        t2 = HH2 * 60 + MM2

        diff = t2 - t1
        playtime = int(playtime)

        if playtime <= diff:
            # 현재 과제 완료
            answer.append(name)

            # 다음 과제 시작까지 남은 시간
            possible = diff - playtime

            # 남은 시간 동안 중단된 과제 처리
            while stack and possible > 0:
                s, t = stack.pop()

                if t <= possible:
                    answer.append(s)
                    possible -= t
                else:
                    stack.append((s, t - possible))
                    possible = 0

        else:
            # 끝내지 못한 과제의 남은 시간 저장
            stack.append((name, playtime - diff))

    # 마지막 과제 완료
    answer.append(plans[-1][0])

    # 중단된 과제들을 최근 순서대로 완료
    while stack:
        s, t = stack.pop()
        answer.append(s)

    return answer