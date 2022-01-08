def is_VPS(ps):
    stack = []
    for s in ps:
        if s  == "(":
            stack.append(s)
        else:
            if stack:
                last_bracket = stack.pop()
            else:
                return "NO"

    if stack:
        return "NO"
    else:
        return "YES"

T = int(input())

for _ in range(T):
    s = input()
    print(is_VPS(s))
