import sys
# 
sys.stdin=open("input.txt", "r")
arr=[]
def DFS(v,n):
    if v>n: # 노드 최대값이 7이기 때문
        return
    else:
        # print(v, end=' ') # 전위 순회
        arr.append(v)
        DFS(v+1,n) # 왼쪽 노드
        print(arr) # 중위 순회
        arr.remove(v)
        DFS(v+1,n) # 오른쪽 노드
        # print(v) # 후위 순회
        
        


if __name__=="__main__":
  
    n=int(input())
    DFS(1,n)
    
       
   