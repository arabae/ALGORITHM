def solution(brown, yellow):
    if yellow == 1:
        answer = [3, 3]
        return answer  # 예외

    for i in range(1, yellow // 2 + 1):
        if yellow % i == 0:
            j = yellow // i
            if (i + 2) * 2 + (j + 2) * 2 - 4 == brown and i <= j:
                answer = [j + 2, i + 2]

    return answer