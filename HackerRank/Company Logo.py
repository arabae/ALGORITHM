"""
가장 많이 나온 알파벳 3개를 순서대로 개수와 함께 출력
- 만약 개수가 같다면 알파벳순으로
"""

import math
import os
import random
import re
import sys

from collections import Counter

def top3_most_common(s):
    char_cnt = Counter(sorted(s, key=lambda x:ord(x)))
    top3 = char_cnt.most_common(3)
    for k, v in top3:
        print(k, v)

if __name__ == '__main__':
    s = input()
    top3_most_common(s)
