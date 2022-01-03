N = int(input())
weight_height = [list(map(int, input().split())) for _ in range(N)]

bulk_order = []
for i in range(len(weight_height)):
    cnt = 1
    cur_w, cur_h = weight_height[i]
    for j in range(len(weight_height)):
        if i == j: continue
        nxt_w, nxt_h = weight_height[j]
        if cur_w < nxt_w and cur_h < nxt_h:
            cnt += 1

    bulk_order.append(cnt)

for c in bulk_order:
    print(c, end=' ')