import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque()

for _ in range(n):
    s = input().strip()
    if s == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif s == 'size':
        print(len(stack))
    elif s == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif s == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(int(s.split()[-1]))
