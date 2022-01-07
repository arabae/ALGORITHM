def split_balance_bracket_string(s):
    u, v = "", ""
    bracket_dict = {"(": 1, ")": -1}
    balance_check, idx = 0, 0
    for char in s:
        balance_check += bracket_dict[char]
        u += char
        if balance_check == 0:
            break
        idx += 1
    v += s[idx+1:]
    return u, v

def convert_balance_bracket_string(s):
    if is_right_bracket_string(s):
        return s
    
    convert_str = "("
    s = s[1:]
    s = s[:-1]
    
    for char in s:
        if char == "(":
            convert_str += ")"
        else:
            convert_str += "("
    
    convert_str += ")"
    return convert_str

def is_right_bracket_string(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

def recursion_process(p):
    if not p: 
        return p
    
    u, v = split_balance_bracket_string(p)
    if is_right_bracket_string(u):
        return u + recursion_process(v)
    else:
        blank_str = "("
        blank_str += recursion_process(v)
        blank_str += ")"
        
        u = u[1:]
        u = u[:-1]
        
        for sub_u in u:
            if sub_u == "(":
                blank_str += ")"
            else:
                blank_str += "("
        return blank_str
                
def solution(p):
    if not p:
        return p
    answer = recursion_process(p)
    
    return answer