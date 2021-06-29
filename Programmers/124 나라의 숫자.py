def solution(n):
    # 1, 2, 4를 순서대로 사용 (4까지 다 쓰면 옆으로 붙여서 사용)

    num_dict = {1:"1", 2:"2", 0:"4"}
    r = n%3
    n = n//3 if r != 0 else n//3 -1
    answer = num_dict[r]

    while n > 0:
        r = n%3
        n = n//3 if r != 0 else n//3 -1
        answer = num_dict[r] + answer

    return str(answer)
