from collections import deque

N = int(input())
cards = deque([i+1 for i in range(N)])

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])