"""
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분
"""

while True:
    triangle_a, triangle_b, triangle_c = map(int, input().split())
    if triangle_a == 0 and triangle_b == 0 and triangle_c == 0:
        break
    
    triangle_a, triangle_b, triangle_c = triangle_a**2, triangle_b**2, triangle_c**2

    max_side = max(triangle_a, triangle_b, triangle_c)
    sum_side = triangle_a + triangle_b + triangle_c

    sum_side -= max_side

    if sum_side == max_side:
        print("right")
    else:
        print("wrong")
