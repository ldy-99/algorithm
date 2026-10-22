# 프로그래머스 광물캐기(그리디)
def solution(picks, minerals):
    minerals = minerals[:sum(picks) * 5]
    answer = 0
    n = len(minerals)
    scores = []

    for i in range(0, n, 5):
        group = minerals[i:i+5]

        dia = group.count("diamond")
        iron = group.count("iron")

        scores.append((dia, iron, group))

    scores.sort(key=lambda x: (x[0], x[1]), reverse=True)

    idx = 0  # 채굴 그룹 인덱스

    for p, count in enumerate(picks):
        for _ in range(count):
            if idx >= len(scores):
                return answer

            dia, iron, group = scores[idx]
            stone = len(group) - dia - iron

            if p == 0:       # 다이아 곡괭이
                answer += len(group)

            elif p == 1:     # 철 곡괭이
                answer += dia * 5 + iron + stone

            elif p == 2:     # 돌 곡괭이
                answer += dia * 25 + iron * 5 + stone

            idx += 1

    return answer