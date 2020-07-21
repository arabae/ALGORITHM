def kalender(first_month, first_day, second_month, second_day):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = 0
    if first_month == second_month:
        answer = second_day-first_day + 1
    else:
        answer += days[first_month-1] - first_day + 1
        for j in days[first_month:second_month-1]:
            answer += j
        answer += second_day

    return answer


T = int(input())
for i in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    print('#%d %d'%(i, kalender(m1, d1, m2, d2)))