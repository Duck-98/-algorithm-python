import sys
sys.stdin=open("input.txt", "r")

def Count(len):
    cnt=1
    ep=house[0]
    for i in range(1, n):
        if house[i]-ep>=len:
            cnt+=1
            ep=house[i]
        return cnt;
    
n,c = map(int,input().split())
house=[]
for _ in range(n):
    tmp=int(input())
    house.append(tmp)
house.sort()


lt=1
rt=house[n-1]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)