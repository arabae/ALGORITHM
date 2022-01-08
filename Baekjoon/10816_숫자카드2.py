import sys
from collections import defaultdict

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
card_cnt = defaultdict(int)
for c in cards:
    card_cnt[c] += 1

m = int(sys.stdin.readline())
find_cards = list(map(int, sys.stdin.readline().split()))
for f in find_cards:
    print(card_cnt[f], end=' ')