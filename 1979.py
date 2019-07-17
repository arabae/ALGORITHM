def wordPosition(M, w):
    '''
    :param M: Matrix information
    :param w: word length
    :return: count possible positions of word
    '''
    count = 0
    for n in range(len(M)):
        rows = 0
        cols = 0
        for m in range(len(M)):
            if M[n][m] == 1:
                rows += 1
            else:
                if rows == w:
                    count += 1
                rows = 0

            if M[m][n] == 1:
                cols += 1
            else:
                if cols == w:
                    count += 1
                cols = 0

        if rows == w:
            count += 1
        if cols == w:
            count += 1
    return count


T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    matrix = []
    for j in range(N):
        matrix.append(list(map(int, input().split())))

    p = wordPosition(matrix, K)
    print('#%d %d'%(i+1, p))