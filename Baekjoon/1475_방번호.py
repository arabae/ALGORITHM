N = input()
num_check = [0] * 9

for n in N:
    int_n = int(n)
    if int_n == 9: int_n = 6
    num_check[int_n] += 1

max_num = 0
for i, v in enumerate(num_check):
    if i == 6: v = v//2 + v%2
    max_num = max(max_num, v)

print(max_num)
