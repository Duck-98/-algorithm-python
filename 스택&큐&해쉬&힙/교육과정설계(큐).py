import sys
from collections import deque
sys.stdin=open("input.txt", "r")


cnt=0
n=input()
k=int(input())
for i in range(k):
    plan=input()
    dq=deque(n)
    for x in plan:
      if x in dq:
          if x != dq.popleft():
              print("#%d NO"%(i+1))
              break
    else:
        if len(dq)==0:
              print("#%d YES"%(i+1))
        else:
            print("#%d NO"%(i+1))
        