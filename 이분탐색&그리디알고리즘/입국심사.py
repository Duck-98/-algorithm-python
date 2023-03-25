def solution(n, times):
    answer=0
    lt= min(times)
    rt= max(times)*n

    while lt<=rt:
        mid=(lt+rt)//2
        cnt=0
        for i in times:
            cnt+=mid //i
            if cnt >=n:
                break;
        if cnt<n:
            lt=mid+1
        elif cnt>=n:
            answer=mid
            rt=mid-1
    return answer       
            

        
    