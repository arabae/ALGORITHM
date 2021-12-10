"""
N장의 카드를 모두 숫자가 보이도록 놓고, M과 최대한 가깝게 3장의 카드를 골라야 함
M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합
"""

from itertools import combinations
N, M = map(int, input().split())

cards = list(map(int, input().split()))
sum_three_cards = sorted(list(map(sum, combinations(cards, 3))), reverse=True)
max_sum_idx = list(map(lambda x: x <= M, sum_three_cards)).index(True)

print(sum_three_cards[max_sum_idx])