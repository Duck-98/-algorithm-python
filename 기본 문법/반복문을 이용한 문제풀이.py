'''
반복문을 이용한 문제 풀이
1) 1 N까지의 홀수 출력
2) 1 N까지의 합 구하기
3) N의 약수출력하기
'''
'''
n=int(input())
for i in range(1,n+1):
    print(i)
'''
# 1) 1 N까지의 홀수 출력
'''
n=int(input())
for i in range(1,n+1):
    if i%2==1:
        print(i)
'''

# 2) 1 N까지의 합 구하기
'''
n=int(input())
sum = 0
for i in range(1,n+1):
    sum=sum+i
print(sum)
'''

# 3) N의 약수출력하기
n=int(input())

for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')