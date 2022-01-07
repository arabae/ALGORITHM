from collections import defaultdict

def solution(str1, str2):
    answer = 0
    str1_dict, str2_dict = defaultdict(int), defaultdict(int)
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_dict[str1[i:i+2].lower()] += 1
            
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_dict[str2[i:i+2].lower()] += 1
    
    str1_keys, str2_keys = str1_dict.keys(), str2_dict.keys()
    if not str1_keys and not str2_keys:
        answer = 1
    else:
        union = set(str1_keys) | set(str2_keys)
        inter = set(str1_keys) & set(str2_keys)
        
        union_num = sum([max(str1_dict[u], str2_dict[u]) for u in union])
        inter_num = sum([min(str1_dict[i], str2_dict[i]) for i in inter])
        answer = inter_num / union_num
    
    return int(answer * 65536)