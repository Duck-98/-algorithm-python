import sys
sys.stdin=open("input.txt", "r")

n,m = map(int,input().split())
p = list(map(int,input().split()))
cnt=0
boat=0
p.sort()

while p:
    if p[0]+p[-1]>m:
        p.pop()
        cnt+=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1
print(cnt)