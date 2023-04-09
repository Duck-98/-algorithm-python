import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, k=map(int,input().split())
danger=[(pos,Val) for pos, Val in enumerate(list(map(int,input().split())))]
danger=deque(danger)
cnt=0

while True:
    cur=danger.popleft()
    if any(cur[1] < x[1] for x in danger):
        danger.append(cur)
    else:
        cnt+=1
        if cur[0]==k:
            break

print(cnt)

