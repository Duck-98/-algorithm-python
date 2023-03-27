import sys
from collections import deque
sys.stdin=open("input.txt", "r")

n = int(input())
a = list(map(int,input().split()))
arr= deque(a)
tmp=0
res=""
cnt=0
lt=0
rt=n-1



while lt<=rt:
    if a[lt]<last:
        tmp.append((a[lt],'L'))
    if a[rt]>last:
        tmp.append((a[rt],"R"))
    tmp.sort()
    if len(tmp)==0:
        break;
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()