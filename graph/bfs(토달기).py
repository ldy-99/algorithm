import sys
from collections import deque
input = sys.stdin.readline
d , word = input().split()
d = int(d)
dic = set(input().strip() for _ in range(d))

def bfs(word,dic):
    visited = set([word])
    q = deque([word])
    ans = word
    while q:
        W = q.popleft()  #cal
        if len(W) > len(ans):
            ans = W
        for i in range(len(W)+1):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = W[:i] + c + W[i:]
                if new_word in dic and new_word not in visited:
                    q.append(new_word)
                    visited.add(new_word)
    return ans
print(bfs(word,dic))