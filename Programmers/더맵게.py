import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)
        if first_min < K:
            heapq.heappush(scoville, first_min + (2*second_min))
            answer += 1
    return answer