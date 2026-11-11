#프로그래머스 큰수만들기
def solution(number, k):
    stack = []
    for num in number :
        while stack and k > 0 and stack[-1] < num :
            stack.pop()
            k -= 1
        stack.append(num)
    # 9,8,7 과 같은 순서대로 가게 되면 while 문이 실행되지 않는다.
    if k > 0 :  # k가 0이 되면 빈 리스트가 반환되기 때문이다.
        stack = stack[:-k]
    return ''.join(stack)