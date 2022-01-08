def is_balance_bracket(string):
    bracket_pair = {"(": ")", "[": "]"}
    stack = []
    for s in string:
        if s  == "(" or s == "[":
            stack.append(s)
        elif s ==")" or s =="]":
            if stack:
                last_bracket = stack.pop()
                if bracket_pair[last_bracket] != s:
                    return "no"
            else:
                return "no"
        else:
            continue

    if stack:
        return "no"
    else:
        return "yes"

input_string = input()
while input_string != ".":
    answer = is_balance_bracket(input_string)
    print(answer)
    input_string = input()
