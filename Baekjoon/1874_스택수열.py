"""
stack에 push하는 순서는 반드시 오름차순
stack을 이용해 주어진 수열을 만들 수 있는지 확인하고, 있다면 어떤 순서로 push와 pop을 수행하는지 계산
불가능하면 NO, 가능할 때 push는 + pop은 -로 표현
"""

N = int(input())
sequence = [int(input()) for _ in range(N)]
stack, print_stack = [], []
tag_idx = 0

for i in range(1, N+1):
    stack.append(i)
    print_stack.append("+")

    if i == sequence[tag_idx]:
        x = stack.pop(-1)
        while x == sequence[tag_idx]:
            print_stack.append("-")
            tag_idx += 1
            if stack:
                x = stack.pop(-1)
            else:
                break
        
        if x != sequence[tag_idx-1]: stack.append(x)

if stack:
    print("NO")
else:
    [print(p) for p in print_stack]
