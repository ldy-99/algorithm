import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
white , blue = 0 , 0

def sol(x,y,N):
    global white , blue
    color = paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if paper[i][j] != color:  #영역이 같은색인지 확인 
                mid = N//2
                sol(x,y,mid)
                sol(x,y+mid,mid)
                sol(x+mid,y,mid)
                sol(x+mid,y+mid,mid)
                return
    if color == 0:
        white +=1
    else:
        blue +=1

sol(0,0,N)
print(white)
print(blue)