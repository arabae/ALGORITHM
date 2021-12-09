"""
입력받은 board를 8x8로 자른 뒤,
체스판이 되기 위해 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램

0,0 0,1 0,2 0,3  처음이 B이면 (짝,짝)과 (홀,홀)이 모두 B이고 (홀,짝),(짝,홀)은 모두 W
1,0 1,1 1,2 1,3  반대의 경우도 같음
2,0 2,1 2,2 2,3
3,0 3,1 3,2 3,3

따라서, (짝,짝)/(홀,홀)과 (홀,짝),(짝,홀)이 각각 다른 색깔인걸 check
"""
n, m = map(int, input().split())
max_r, max_c = n-8, m-8
board = [input() for _ in range(n)]

n_changes = float('inf')

for i in range(max_r+1):
    for j in range(max_c+1):
        w_change, b_change = 0, 0
        for ridx in range(i, i+8):
            for cidx in range(j, j+8):
                if (ridx+cidx)%2==0 and board[ridx][cidx] == 'B': # 짝이 W일때,
                    w_change +=1
                elif (ridx+cidx)%2==0 and board[ridx][cidx] == 'W': # 짝이 B일때,
                    b_change +=1
                elif (ridx+cidx)%2==1 and board[ridx][cidx] == 'B': # 짝이 B일때,
                    b_change +=1
                else: # 짝이 W일때,
                    w_change +=1

        change = min(w_change, b_change)
        n_changes = min(n_changes, change)

print(n_changes)