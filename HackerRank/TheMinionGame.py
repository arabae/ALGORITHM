# 10^6 -> 1,000,000 -> O(n) or O(n*log(n))

def minion_game(string):
    points = {"Stuart":0, "Kevin":0}
    n_string = len(string)
    for idx, val in enumerate(string):
        print(val)
        if val in "AEIOU":
            points["Kevin"] += n_string - idx
        else:
            points["Stuart"] += n_string - idx

    if points['Stuart'] == points['Kevin']:
        print('Draw')
    else:
        winner = "Stuart" if points['Stuart'] > points['Kevin'] else "Kevin"
        winner_score = points[winner]
        print(winner, winner_score)


if __name__ == '__main__':
    # s = input()
    s = "BANANA"
    minion_game(s)