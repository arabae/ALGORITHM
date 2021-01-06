def solution(priorities, location):
    answer = 0
    poi = priorities[location]
    unique_prior = sorted(list(set(priorities)), reverse=True)
    dic = dict()
    
    for i in range(len(unique_prior)):
        key_value = []
        for j in range(len(priorities)):
            if unique_prior[i] == priorities[j]:
                key_value.append(j)
        dic[unique_prior[i]] = key_value

    high_prior_last = -1
    for key, val in dic.items():
        num_val, new_position = len(val), 0
        for i in range(num_val):
            if high_prior_last < val[i]:
                new_position = i
                break
        tmp, val = val[:new_position], val[new_position:]
        val.extend(tmp)

        if key != poi:
            answer += num_val
        else:
            for i in range(num_val):
                answer += 1
                if val[i] == location:
                    break
            break
        high_prior_last = val[-1]
    return answer