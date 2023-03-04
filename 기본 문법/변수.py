'''
변수명 정하기
1. 영문과 숫자, _로 이루어짐
2. 대소문자를 구분
3. 문자나, _로 시작할 수 있음
4. 특수문자 사용 안됨
5. 키워드 사용하면 안됨 (if,for)
'''

a=1
A=2

print(a,A)

a, b, c=3, 2, 1
print(a,b,c)
# 3 2 1
print(a,b,c, sep=',')
#3,2,1
print(a,b,c, sep='\n')
'''
3
2
1
'''
print(a, end=' ')
print(b, end=' ')
print(c)
# 3 2 1

#값 교환
a, b = 10, 20
print(a,b)
# 10 20
a, b = b, a
print(a,b)
# 20 10

# 변수 타입
a=12345
print(type(a))
#<class 'int'>
