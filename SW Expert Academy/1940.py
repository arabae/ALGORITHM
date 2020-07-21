def goRC(cmd, s):
    v = 0
    distance = 0
    for k in range(s):
        if cmd[k][0] == 1:
            v += cmd[k][1]
            distance += v
        elif cmd[k][0] == 2:
            if cmd[k][1] >= v:
                v = 0
            else:
                v -= cmd[k][1]
            distance += v
        else:
            distance += v
    return distance


T = int(input())
for i in range(T):
    N = int(input())
    temp = []
    command = []
    for j in range(N):
        temp.append(input())
        if temp[j] != 0:
            command.append(list(map(int, temp[j].split())))
        else:
            command.append(list(int(command[j])))
    result = goRC(command, N)
    print('#%d %d'%(i+1, result))