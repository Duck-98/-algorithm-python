import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
print(n)
res=0
for i in range(n):
    tmp = input().split()
    tmp.sort() # 작은 값부터 나오도록 순서변경
    a, b, c= map(int,tmp)
    if a==b and b==c:
        money=10000+(a*1000)
    elif a==b or a==c: 
        money=1000+(b*100)
    else:
        money=c*100
    if money>res:
        res=money
print(res)