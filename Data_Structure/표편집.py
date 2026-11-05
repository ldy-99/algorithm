# 프로그래머스 표 편집(카카오)
# 데이터를 실제로 삭제하거나 삽입하지 않고, 연결 관계만 변경하여 삭제와 복구를 O(1)에 처리하는 것
# 삭제한 행과 연결 정보를 스택으로 저장하는 것. prev 와 nxt 사용에 유심히 보자.

def solution(n,k,cmd):
    prev = [i-1 for i in range(n)]
    nxt = [i+1 for i in range(n)]
    cursor = k
    delete_stack = []
    
    answer = ['O'] * n
    
    for c in cmd :
        c = c.split()
        command = c[0]
        
        if command == 'U' : # 위 X 칸
            x = int(c[1])
            for _ in range(x):
                cursor = prev[cursor]
                
        elif command == 'D' : # 아래 X 칸
            x = int(c[1])
            for _ in range(x):
                cursor = nxt[cursor]
                
        elif command == 'C' :  # 현재 선택된 행 삭제 후 아래 행 선택 or 마지막 행 삭제시 바로 윗 행
            pre_node = prev[cursor]
            nxt_node = nxt[cursor]
            
            delete_stack.append((cursor , pre_node , nxt_node))  # 삭제되는 정보를 스택에 저장
            answer[cursor] = 'X'
            
            if pre_node != -1 : # 이전 행 존재함
                nxt[pre_node] = nxt_node  # (이전 행 다음 노드) change (현재 행 다음 노드)
            
            if nxt_node != n : # 다음 행 존재함
                prev[nxt_node] = pre_node # (다음 행 이전노드) change (현재 행 이전 노드)
            
            cursor = pre_node if nxt_node == n else nxt_node

        elif command == 'Z' :
            d_cursor , pre_node , nxt_node = delete_stack.pop()
            answer[d_cursor] = 'O'
            
            # 행 복구  ex) 1 2(복구) 3
            if pre_node != -1 :
                nxt[pre_node] = d_cursor
            
            if nxt_node != n :
                prev[nxt_node] = d_cursor
                
    return ''.join(answer)