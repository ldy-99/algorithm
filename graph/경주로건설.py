# 프로그래머스 경주로건설

def solution(board):
    answer = 0    
    N = len(board)
    INF = float('inf')
    cost = [[[INF] * 4 for _ in range(N)] for _ in range(N)]

    return answer