def calcul_quiz_score(answer):
    cnt, score = 0, 0
    for a in answer:
        if a == 'O':
            cnt += 1
        else:
            cnt = 0
        score += cnt
    return score

T = int(input())
for _ in range(T):
    quiz_result = input()
    quiz_score = calcul_quiz_score(quiz_result)
    print(quiz_score)