'''
리스트와 내장함수(1)
'''
import random as r
a=[]
b=list()

a=[1, 2, 3, 4, 5]
# print(a)

b=list(range(1, 11)) # b에 1~10까지의 리스트를 만들어줌
# print(b)
c=a+b # 리스트 합치기
# print(c)

print(a)
a.append(6) # 맨 뒤에 값 추가
print(a)

a.insert(3, 7) # 3번 인덱스에 7을 추가해줌
print(a)
a.pop() # 맨 뒤 값 제거
print(a)
a.remove(4) # 해당 값 제거
print(a)

print(a.index(5)) # 해당 값의 Index 번호 출력
a=list(range(1, 11))
print(a)
print(sum(a)) # sum => 리스트의 모든 값들을 합쳐줌
print(max(a)) # 제일 큰 값 출력
print(min(a)) # 제일 작은 값 출력
print(min(7, 5)) 

r.shuffle(a) # 무작위로 섞어주는 함수
print(a)

a.sort(reverse=True)  # 내림차순 정렬
print(a)

a.sort() # 오름차순 정렬
print(a)
