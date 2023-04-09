from collections import deque

arr = deque([i for i in range(1,int(input())+1)])
while arr:
    print(arr.popleft(),end=" ")
    if arr:
        arr.append(arr.popleft())