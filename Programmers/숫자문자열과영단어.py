def solution(s):
    convert_num = []
    num_eng_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 
                    'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    word = ''
    for c in s:
        if c.isdigit():
            convert_num.append(c)
        else:
            word += c
            if word in num_eng_dict.keys():
                convert_num.append(num_eng_dict[word])
                word = ''
    
    convert_num = ''.join(convert_num)
    return int(convert_num)
