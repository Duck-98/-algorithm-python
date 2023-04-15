import sys

sys.stdin=open("input.txt", "r")

def func(n):
    if n==0:
        return
    else:
       func(n//2)
       print(n%2, end='')


if __name__=="__main__":
    n=int(input())
    func(n)