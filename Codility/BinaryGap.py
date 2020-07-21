# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    bin_N = bin(N)[2:]
    find_one, binary_gap = [], []
    [find_one.append(x) for x in range(len(bin_N)) if bin_N[x] == '1']
    for i in range(len(find_one)-1): binary_gap.append(find_one[i+1]-find_one[i]-1)
    if binary_gap:
        return max(binary_gap)
    else:
        return 0
