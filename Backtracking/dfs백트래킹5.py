import sys
input = sys.stdin.readline

mo = {'a','e','i','o','u'}

def dfs(depth,start,password):
    if depth == L:
        mocnt = sum(1 for i in password if i in mo)
        jacnt = L - mocnt
        
        if mocnt >= 1 and jacnt >= 2 :
            print("".join(password))
        return
    
    for i in range(start,C):
        password.append(letters[i])
        dfs(depth+1 , i+1 , password)
        password.pop()
        
L,C=map(int,input().split())
letters = sorted(input().split())
dfs(0,0,[])