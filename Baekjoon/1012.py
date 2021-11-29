def search_neighbor(q):
    while q:
        x, y, location = q.pop(0)

        if y + 1 < N and location[y + 1][x] == 1:  # 상
            location[y+1][x] = 0
            q.append((x, y + 1, location))
        if y - 1 >= 0 and location[y - 1][x] == 1:  # 하
            location[y - 1][x] = 0
            q.append((x, y - 1, location))
        if x + 1 < M and location[y][x + 1] == 1:  # 좌
            location[y][x + 1] = 0
            q.append((x + 1, y, location))
        if x - 1 >= 0 and location[y][x - 1] == 1:  # 우
            location[y][x - 1] = 0
            q.append((x - 1, y, location))


T = int(input()) # 테스트 케이스 수

for _ in range(T):
    M, N, K = map(int, input().split())  # 배추밭 가로, 세로, 심어진 배추 개수
    location = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        location[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if location[i][j]: # 배추가 있으면
                search_neighbor([(j, i, location)])
                cnt += 1
    print(cnt)
