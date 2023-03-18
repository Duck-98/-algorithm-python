import sys
sys.stdin=open("input.txt", "rt")
large = -2190000
n = int(input());

a=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j] # 행
        sum2+=a[j][i] # 열
    if sum1>large:
       large=sum1
    if sum2>large:
       large=sum2
sum1=sum2=0
for i in range(n):
   sum1+=a[i][i] # 왼쪽 시작 대각선
   sum2+=a[i][n-i-1] # 오른쪽 시작 대각선
if sum1>large:
    large=sum1
if sum2>large:
    large=sum2 
print(large)