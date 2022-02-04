A = int(input()) # 고기의 원래 온도
B = int(input()) # 목표 온도
C = int(input()) # 얼어 있는 고기를 1도 데우는데 걸리는 시간
D = int(input()) # 얼어 있는 고기를 해동하는 데 걸리는 시간
E = int(input()) # 얼어 있지 않은 고기를 1도 데우는데 걸리는 시간

times = 0
while A != B:
    if A < 0:
        times += C
    else:
        if A == 0:
            times += D
        times += E
    A += 1

print(times)