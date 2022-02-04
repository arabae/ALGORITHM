B1 = input() # 이진수
B2 = input() # 이진수

multiple = bin(int(B1, 2) * int(B2, 2))[2:]
print(multiple)
