import sys
sys.stdin=open("input.txt", "rt")
dx=[-1,0,1,0]
dy=[0,1,0,-1]
res=0

n = int(input());
a=[list(map(int,input().split())) for _ in range(n)]

a.insert(0,[0]*n)
a.append([0]*n)
for i in range(n+2):
    a[i].insert(0,0)
    a[i].append(0)
print(a[0][1],a[2][1])
for i in range(1,n+1):
   for j in range(1,n+1):
       if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
           res+=1

print(res)
           
           
            
       
   

