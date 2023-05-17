import sys 
sys.stdin=open("input.txt", "r")

def DFS(L, res):
   if res>total//2:
       return
   
   if L==n :
       if res==(total-res):
           print("YES")
           sys.exit(0)
   else:
       DFS(L+1, res+a[L])
       DFS(L+1, res)
       
    
       

         


if __name__=="__main__":
    n=int(input())
    a = list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
    print("NO")
    
       
   