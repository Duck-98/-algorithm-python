'''
리스트와 내장함수(2)
'''
a=[23, 12 ,36, 53, 19]
print(a[:3])
for i in range(len(a)):
    print(a[i])
# 둘이 같은 결과
for x in a:
    print(x)
    

for x in a:
    if x%2==1:
        print(x)
print()
for x in enumerate(a): # 인덱스번호와 해당 값이 같이 출력 ex) (0,23)
    print(x[0], x[1])
print()
# 둘이 같은 결과
for index, value in enumerate(a):
    print(index,value)

print()
# if any(15>x for x in a):  -> 모든 조건이 성립해야 참이나옴
if any(15>x for x in a): # 조건 중 하나라도 성립하면 참이 나옴
    print("Yes")
else:
    print("NO")