'''
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연
수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
평균은 소수 첫째 자리에서 반올림합니다.
'''

import sys
sys.stdin=open("input.txt", "rt")

n=int(input()) 
c=0
a = list(map(int,input().split()))
for i in range(n):
    c+=a[i]
c= round(c/10)    
min=float('inf')

for idx ,x in enumerate(a): # enumerate는 배열의 값과 INDEX값을 두개 다 비교해주게 해줌.
    tmp=abs(x-c) # abs -> 절대값구하는 함수
    if tmp<min:
        min=tmp
        score=x
        res=idx+1 #0번부터 시작했기 때문에 +1
    elif tmp==min:  # 점수값이 같을 때
        if x>score: # x==score로 하면 같은 값중에 맨 뒤에 값이 답이 됨.
            score=x
            res=idx+1
        
print(c, res)
