def solution(answers):
    # 1번과 2번은 1~5순서로 찍지만, 2번은 앞에 2가 한번씩 더 추가
    # 3번은 3, 1, 2, 4, 5로 2번씩 찍음
    pick = [[1, 2, 3, 4, 5], [1, 3, 4, 5], [3, 1, 2, 4, 5]]
    hit_cnt = [0, 0, 0]

    for i, v in enumerate(answers):
        if v == pick[0][i%5]:
            hit_cnt[0] +=1

        student2 = pick[1][(i-1)%8//2] if i%2 == 1 else 2

        if v == student2:
            hit_cnt[1] +=1

        if v == pick[2][((i-(i%2))//2)%5]:
            hit_cnt[2] +=1

    max_cnt = max(hit_cnt)
    answer = [i+1 for i in range(3) if max_cnt == hit_cnt[i]]
    return answer