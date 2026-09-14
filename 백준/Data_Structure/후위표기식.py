#후위 표기식 1918번
import sys
input = sys.stdin.readline

infix = input().strip()
pre = {'+':1 ,'-':1,'*':2,'/':2}

stack = []
ans = []

for c in infix :
    if c.isalpha():
        ans.append(c)
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(' :
            ans.append(stack.pop())
        stack.pop()
    else:
        while (stack and stack[-1] != '(' and pre.get(c,0) <= pre.get(stack[-1],0)):
            ans.append(stack.pop())
        stack.append(c)
while stack:
    ans.append(stack.pop())

print(''.join(ans))