def dfs(val, idx, n_list, num, targetNum):    # value, index, list, targetNumber
    # 만약 index 가 리스트의 마지막까지 왔다면 타겟과 비교하여 T/F
    if idx >= n_list:
        if val == targetNum:
            return 1
        else:
            return 0
    res = 0
    res += dfs(val+num[idx], idx+1, n_list, num, targetNum)
    res += dfs(val-num[idx], idx+1, n_list, num, targetNum)
    return res


def solution(numbers, target):
    answer = 0
    n_numbers = len(numbers)
    pr_idx, pr_val = 0, numbers[0]
    # 0번째 index 는 수헹하였으므로 현재 index 보다 1큰 값을 매개변수로 넣음
    answer += dfs(pr_val, pr_idx+1, n_numbers, numbers, target)
    answer += dfs(-pr_val, pr_idx+1, n_numbers, numbers, target)
    return answer


def other_solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return other_solution(numbers[1:], target-numbers[0]) + other_solution(numbers[1:], target+numbers[0])

print(solution([1, 1, 1, 1, 1], 3))