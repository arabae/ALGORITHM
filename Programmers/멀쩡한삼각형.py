def solution(w,h):
    a = -h/w

    if w == 1 or h == 1:
        return 0
    elif w == h:
        return w*h - h
    else:
        answer = 0
        for i in range(1, w+1):
            answer += int(i*a + h)
        return answer*2
