import sys
sys.stdin=open("input.txt", "r")

L = int(input())
box = list(map(int,input().split()))
M = int(input())
box.sort()
print(box)

for _ in range(M):
    box[0]+=1
    box[L-1]-=1
    box.sort()
print(box[L-1]-box[0])
            
      
            
