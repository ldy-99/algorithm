import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

R = []

for c in S:
    R.append(c)

    while True:
        removed = False
        length = len(R)
        
        if length >= 2 and R[-1] == R[-2]:
            R.pop()
            R.pop()
            removed = True

        elif length >= 3 and R[-1] == R[-3]:
            R.pop()
            R.pop()
            R.pop()
            removed = True

        if not removed:
            break
if not R:
    print(-1)
else:
    print(''.join(R))

# 이 문제에서 길이가 4인 팰린드롬은 존재 할 수 없다.