def solution(s):
    stack = []
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
    if stack:
        return 0
    else:
        return 1