def solution(picks, minerals):
    minerals = minerals[:sum(picks) * 5]
    answer = 0
    n = len(minerals)
    scores = []

    weight = {"diamond": 25, "iron": 5, "stone": 1}

    for i in range(0, n, 5):
        group = minerals[i:i+5]

        score = 0
        for mineral in group:
            score += weight[mineral]

        scores.append((score, group))

    scores.sort(reverse=True, key=lambda x: x[0])

    return answer