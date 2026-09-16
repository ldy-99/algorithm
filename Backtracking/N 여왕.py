import sys
input = sys.stdin.readline
def sol(N,y,width,d1,d2): #d1 우하향 d2 우상향
  ans=0
  if y==N :
    ans +=1
  else:
    for i in range(N):  # y번째 행에 i번째 열에 퀸을 놓을건지
      if width[i] or d1[i+y] or d2[i-y+ N]: # 열 , 대각선 확인
        continue
      width[i] = d1[i+y] = d2[i-y+N] = True
      ans += sol(N,y+1,width,d1,d2) 
      width[i] = d1[i+y] = d2[i-y+N] = False  # y+1 다음 행으로 이동한 뒤 백트래킹(False)
  return ans
N = int(input())
ans = sol(N,0, [False]* N , [False]* (N*2) , [False] * (N*2)) 
# 대각 배열은 2N의 크기 -> d1[i+y] 는 최댓값이 2N-2  d2[i-y+N] 은 음수인덱스 방지를 위해 +N 을 하고 최댓값은 2N+2
print(ans)