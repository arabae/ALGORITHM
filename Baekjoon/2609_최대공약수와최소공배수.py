num1, num2 = map(int, input().split())
if num1 > num2:
    num1, num2 = num2, num1

# 최대공약수
gcd = 1
for i in range(2, num1+1):
    if num1%i == 0 and num2%i == 0:
        gcd = i
print(gcd)

# 최소공배수
multiple_num1, multiple_num2 = num1, num2
while multiple_num1 != multiple_num2:
    if multiple_num1 < multiple_num2:
        multiple_num1 += num1
    else:
        multiple_num2 += num2

print(multiple_num1)
