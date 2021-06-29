def solution(record):
    # Leave 후 Enter 그리고, Change 에서만 닉네임이 변경됨
    # UserID에 따라 닉네임을 정해두고, 최종 결과를 다시 읽으면서 print
    answer = []

    user_nickname = dict()
    for log in record:
        split_log = log.split(" ")
        if split_log[0] != "Leave":
            user_nickname[split_log[1]] = split_log[2]

    for log in record:
        split_log = log.split(" ")
        state, user_id = split_log[0], split_log[1]

        if state == "Enter":
            answer.append(f"{user_nickname[user_id]}님이 들어왔습니다.")
        elif state == "Leave":
            answer.append(f"{user_nickname[user_id]}님이 나갔습니다.")

    return answer
