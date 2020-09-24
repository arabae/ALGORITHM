def find_values(lists, target):
    return [i for i, v in enumerate(lists) if v == target]


def solution(n, computers):
    parent = [i for i in range(n)]  # 각 computer 가 속해있는 network 의 번호
    for i in range(n):
        connect = find_values(computers[i], 1)  # 1번 컴퓨터부터 연결되어 있는 다른 컴퓨터를 탐색
        connect_parent = set([parent[c] for c in connect])  # 연결된 컴퓨터들이 속한 network 의 중복되지 않은 번호
        min_val = min(connect_parent)   # 그 중 가장 작은 값 (큰 값도 가능), 하나의 network 로 바꾸려고

        for j in connect_parent:    # 현재 연결되어있는 network 에 연결되어있는 모든 컴퓨터를 찾음
            find_parent = find_values(parent, j)
            for k in find_parent:   # 각 network 에 연결된 모든 컴퓨터를
                parent[k] = min_val # min value network 로 이동
    answer = len(set(parent))   # 이동시키고 남은 network 의 개수
    return answer


def old_solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        connect = find_values(computers[i], 1)
        connect_parent = set([parent[c] for c in connect])
        min_val = min(connect_parent)
        
        # 바꾸려는 값에 해당하는 모든 부모값을 바꿔줘야함 numpy를 이용하면 더 간단해질 것 --> 실수한 부분
        for j in connect_parent:
            parent[j] = min_val
    answer = len(set(parent))
    return answer


print(solution(1, [[1]]))
print(solution(4, [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1]]))
print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]))
print(solution(5, [[1, 0, 1, 0, 1], [0, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 1]]))