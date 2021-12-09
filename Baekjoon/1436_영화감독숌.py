"""
- 종말의 숫자: 6이 적어도 3개이상 연속으로 들어가는 수 (666; 종말을 나타내는 숫자)
- 제일 작은 종말의 숫자: 666 (이후 1666, 2666, 3666 ...)
- N번째 영화 제목에 들어간 숫자를 출력
"""

N = int(input())
serise_number = 666

while N:
    if '666' in str(serise_number):
        N -= 1
    serise_number += 1

print(serise_number-1)
