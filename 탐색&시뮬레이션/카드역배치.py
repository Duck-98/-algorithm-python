import sys
sys.stdin=open("input.txt", "rt")
cards=list(range(21))
for _ in range(10): #_ -> 한 줄 마다 불러오기
    a, b = map(int,input().split())
    for i in range((b-a+1)//2):
       cards[a+i],cards[b-i]=cards[b-i],cards[a+i]

cards.pop(0) # 맨 앞자리 배열 제거
for x in cards:
    print(x, end=' ')