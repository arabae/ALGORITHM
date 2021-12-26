"""
n개 원소를 갖는 int형 array의 원소가 set A에 속하면 +1, set B에 속하면 -1
"""

from collections import Counter

n, m = map(int, input().split())
n_array = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

array_map = Counter(n_array)

in_A = set(A).intersection(set(n_array))
in_B = set(B).intersection(set(n_array))

happines = sum([array_map[a] for a in in_A]) - sum([array_map[b] for b in in_B])
print(happines)
