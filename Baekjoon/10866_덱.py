import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deque_ = deque()

for _ in range(n):
    d = input().strip()
    x = -2

    if d == 'pop_front':
        x = deque_.popleft() if deque_ else -1
    elif d == 'pop_back':
        x = deque_.pop() if deque_ else -1
    elif d == 'size':
        x = len(deque_)
    elif d == 'empty':
        x = 0 if deque_ else 1
    elif d == 'front':
       x = deque_[0] if deque_ else -1
    elif d == 'back':
        x = deque_[-1] if deque_ else -1
    else:
        if 'back' in d:
            deque_.append(d.split()[-1])
        else:
            deque_.insert(0, d.split()[-1])

    if x != -2:
        print(x)
