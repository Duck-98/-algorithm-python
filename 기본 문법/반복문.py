'''
반복문 for, while
'''
'''
a=range(10)
print(list(a))
# 리스트 0~9까지 만들어줌.
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a=range(1,11)
print(list(a))
'''
'''
for i in range(1,11):
    print(i)


for i in range(10,0,-2):
    print(i)

2씩 작아짐
10
8
6
4
2
'''
'''
i=1
while i<=10:
    print(i)
    i=i+1
'''
'''
i=10
while i>=1:
    print(i)
    i=i-1
'''
'''
i=1
while True:
    print(i)
    if i==10:
        break
    i+=1

'''

'''
for i in range(1, 11):
    if i%2==0:
        continue # 위에 조건문이 참이면 밑에 줄 무시
    print(i)
# 홀수만 출력
'''

for i in range(1, 11):
    print(i)
    if i==5:
        break
else:
    print(11)
# break를 안하고 정상적으로 출력되면 else문 11까지 출력