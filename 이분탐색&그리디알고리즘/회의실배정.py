# 그리디 알고리즘
import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
meet=[]
for i in range(n):
    s,e = map(int,input().split())
    meet.append((s,e))

meet.sort(key=lambda x: (x[1], x[0]))
et=0
cnt=0
for s,e in meet:
    if s>=et:
        et=e
        cnt+=1
print(cnt)
