# 프로그래머스 수식 최대화
# 순열 활용 문제
# "100-200*300-500+20" -> max = 60420

from itertools import permutations as p
def solution(expression):
    answer = 0
    op = set()
    tokens = []
    num = ''
    for e in expression :
        if e in '+-*' :
            op.add(e)
            tokens.append(int(num))
            tokens.append(e)
            num = ''
        else:
            num += e
    tokens.append(int(num))
    
    # 연산자 우선순위 결정
    for order in p(op) :
        temp = tokens[:]  # 원본 리스트 훼손 방지
        for oper in order :
            while oper in temp :
                i = temp.index(oper)
                a = temp[i-1]
                b = temp[i+1]
                if oper == '+' :
                    result = a + b
                elif oper == '-' :
                    result = a - b
                else :
                    result = a * b
                temp[i-1:i+2] = [result]
        answer = max(answer , abs(temp[0]))
    return answer