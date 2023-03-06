'''
문자열과 내장함수
'''

msg="It is Time"
print(msg.upper()) # 모든 문자 대문자로 바꾸는 함수
print(msg.lower()) # 모든 문자 소문자로 바꾸는 함수
tmp = msg.upper()
print(tmp)
print(tmp.find('T')) # 찾고 싶은 단어의 Index 번호를 찾아줌.
print(tmp.count('T'))# 찾고 싶은 단어의 개수를 구해줌.
print(msg)
print(msg[:2]) # 0~1번까지의 단어만 출력해줌
print(msg[3:5]) # 3~4번까지의 단어만 출력해줌
print(len(msg)) # 문장의 길이를 출력해줌
for i in range(len(msg)):
    print(msg[i], end=' ')
print()
## 둘이 같은 결과 출력
for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper(): # 대문자인 것만 찾아주는 함수
        print(x, end=' ')
print()

for x in msg:
    if x.islower(): # 소문자인 것만 찾아주는 함수
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha(): # 알파벳만 찾아주는 함수
        print(x, end=' ')
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) # ord => 아스키넘버를 출력해주는 함수

tmp='az'
for x in tmp:
    print(ord(x)) # ord => 아스키넘버를 출력해주는 함수
    
tmp=65
print(chr(tmp)) # 아스키넘버와 맞는 문자를 출력해주는 함수