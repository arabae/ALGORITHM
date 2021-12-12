"""
높이가 V미터인 나무막대에 올라가는데, 낮에 A미터 올라가고 밤에 B미터 미끄러짐
나무 막대를 모두 올라가려면 며칠이 걸리는가
"""

A, B, V = map(int, input().split())
days, diff_height = 1, A - B

V -= A
if V <= 0:
    print(days)
else:
    if V % diff_height == 0:
        print(days + V // diff_height)
    else:
        print(days + V // diff_height + 1)
