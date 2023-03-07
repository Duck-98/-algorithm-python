
def func(p,q):
    cnt=0
    for i in range(1, p+1):
        if p%i==0:
            cnt+=1
        if cnt==q:
            print(i)
            break
    else:
        print(-1)
        
        
func(6,3)