'''
변수 입력과 연산자
'''
'''
a=input("숫자를 입력하세요 : ")
# 직접 입력할 수 있음
print(a)
'''
'''
a, b=input("숫자를 입력하세요 : ").split()
print(a+b)
# string 형식이기때문에 덧셈이 아닌 문자열끼리 붙어서 나옴
'''
'''
a, b=input("숫자를 입력하세요 : ").split()4
a=int(a)
b=int(b)
print(a+b)
# 숫자형으로 바꿨기 때문에 연산을 해줌
'''
a, b=map(int, input("숫자를 입력하세요 : ").split())
# 한번에 a,b를 숫자형으로 바꿔줌
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
# 나눠서 몫 구해주는 연산
print(a%b)
# 나눠서 남은 나머지를 구해주는 연산
print(a**b)
# 거듭 제곱
a=4.3
b=6
c=a+b
# c의 타입은 실수형으로 나옴.
# 형이 다른 것끼리 연산을 하면 큰 범위를 갖고 있는 형으로 나옴.