def solution(progresses, speeds):
    answer, finish_time = [], []
    n_progresses = len(progresses)
    for ix in range(n_progresses):
        day = (100 - progresses[ix])//speeds[ix]
        time = 1 if (100 - progresses[ix])%speeds[ix] else 0
        finish_time.append(day+time)
        
    ix = 0
    
    while ix < n_progresses:
        with_release = 1
        for jx in range(ix+1, n_progresses):
            if finish_time[ix] < finish_time[jx]:
                break
            with_release += 1
        answer.append(with_release)
        ix += with_release
    return answer