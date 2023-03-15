import sys
import re
sys.stdin=open("input.txt", "rt")
answer=""
a = input()
arr = re.findall(r'\d', a)
num = int(''.join(map(str, arr)))
cnt=1
for i in range(1,num):
    if num%i==0:
        cnt+=1
print(num)
print(cnt)

res = 0

for x in a:
    if x.isdecimal():
        res=res*10+int(x)
print(res)
cn = 0
for i in range(1, res+1):
    if res%1==0:
        cn+=1
print(cnt)