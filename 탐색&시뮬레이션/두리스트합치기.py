import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
p1=p2=0
answer=[]
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        answer.append(a[p1])
        p1+=1
    elif a[p1]>b[p2]:
        answer.append(b[p2])
        p2+=1
if p1<n:
    answer=answer+a[p1:]
else:
    answer=answer+b[p2:]

for x in answer:
    print(x, end= ' ')