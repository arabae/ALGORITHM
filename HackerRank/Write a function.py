"""
윤년인지 아닌지 True/False로 출력
- 윤년은 4로 나누어 떨어짐
- 100으로 나누어 떨어지면 윤년이 아님
    - 단, 400으로 나누어 떨어지면 윤년
"""

def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 != 0:
            leap = True
        elif year%100 == 0 and year%400 == 0:
            leap = True
    return leap

year = int(input())
print(is_leap(year))