import sys
sys.stdin=open("input.txt", "rt")
n = int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1

print(cnt)



def primes_sieve(num):
    is_prime = [True] * (num + 1)
    for i in range(2, int(num**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, num+1, i):
                is_prime[j] = False
    return [i for i in range(2, num+1) if is_prime[i]]




