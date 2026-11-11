#프로그래머스 큰수만들기
def solution(number, k):
    stack = []
    for num in number :
        while stack and k > 0 and stack[-1] < num :
            top = stack.pop()
            print(top)
            k -= 1
        stack.append(num)
    # 9,8,7 과 같은 순서대로 가게 되면 while 문이 실행되지 않는다.
    if k > 0 :  # k가 0이 되면 빈 리스트가 반환되기 때문이다.
        stack = stack[:-k]
    return ''.join(stack)

number = "1129"
k = 2
print(solution(number,k))

# 가장 큰 수를 만들려면 앞자리 숫자가 최대한 커야 한다.
# 숫자를 왼쪽부터 확인하면서 스택에 저장한다.
# 현재 숫자가 스택의 마지막 숫자보다 크다면, 제거 횟수가 남아 있는 동안 작은 숫자를 제거한다.
# 현재 숫자를 스택에 추가한다.
# 모든 숫자를 처리했는데 제거 횟수가 남았다면 뒤에서 제거한다.