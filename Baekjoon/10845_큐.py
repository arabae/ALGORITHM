import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    q = input().strip()
    if q == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif q == 'size':
        print(len(queue))
    elif q == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif q == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif q == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)  
    else:
        queue.append(int(q.split()[-1]))
