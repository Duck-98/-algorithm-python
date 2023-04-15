import sys
# 1~7까지로 이루어져 있는 트리를 출력하는 알고리즘
sys.stdin=open("input.txt", "r")

def DFS(v):
    if v>7: # 노드 최대값이 7이기 때문
        return
    else:
        print(v, end=' ') # 전위 순회
        DFS(v*2) # 왼쪽 노드
        print(v, end=' ') # 중위 순회
        DFS(v*2+1) # 오른쪽 노드
        print(v, end=' ') # 후위 순회
        
        


if __name__=="__main__":
    DFS(1)