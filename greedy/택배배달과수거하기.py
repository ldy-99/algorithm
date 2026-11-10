# 프로그래머스 택배배달과 수거하기
# 배달과 수거의 남은 물량 각각 관리한다.
# 가장 먼 집에 물량이 남아있다면 , 여러번 왕복해야 할 수 있다.(그리디)
# 즉 , 따라서 먼 집에 가는 김에 가까운 집의 작업도 처리하는 것이 유리하다.
def solution(cap, n, deliveries, pickups):
    answer = 0
    dc = 0
    pc = 0
    
    for i in range(n - 1, -1, -1):
        dc += deliveries[i]
        pc += pickups[i]

        while dc > 0 or pc > 0:
            dc -= cap
            pc -= cap
            answer += (i + 1) * 2
    return answer