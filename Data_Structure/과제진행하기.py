# 잘못된 예시
def solution(plans):
    answer = []
    
    plans.sort(key=lambda x: x[1])
    stack = []
    N = len(plans)
    end = plans[-1][0]
    
    for i in range(len(plans)-1):
        name,start,playtime = plans[i]
        nxt = plans[i+1][1]
        
        HH,MM = map(int,start.split(':'))
        HH2,MM2 = map(int,nxt.split(':'))
        
        t1 = HH * 60 + MM
        t2 = HH2 * 60 + MM2
        
        diff = t2 - t1
        if int(playtime) <= diff :
            answer.append(name)
            # 남은 시간에는 중단된 과제를 진행
            if stack :
                s,t = stack.pop()  # 컴퓨터 , 90
                
                # 진행할 수 있는 시간 계산
                possible = diff - int(playtime)
                if t - possible > 0 :
                    stack.append((s,t-possible))
                else:
                    answer.append(s)
        else:
            # 스택 저장 로직
            stack.append((name,int(playtime) - diff))

    while stack :
        s,t = stack.pop()
        answer.append(s)
    return answer