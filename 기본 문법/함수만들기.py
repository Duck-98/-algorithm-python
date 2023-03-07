'''
함수 만들기
'''

def add(a, b):
    c=a+b
    d=a-b
    return c ,d

print(add(1,556))
#(557, -555)
x=add(3,2)
print(x)

a=[12, 13 ,7, 9, 19]

def isPrime(x): # 소수를 구하는 함수
    for i in range(2,x):
        if x%i==0:
            return False
    return True    

for y in a:
    if isPrime(y):
        print(y, end= ' ')