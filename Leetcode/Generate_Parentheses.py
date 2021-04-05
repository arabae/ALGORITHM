import copy


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l, r, state = 0, 0, 0
        s = [['(', l + 1, r, state + 1]]
        result = []
        while s:
            x = s.pop(0)
            # '(' 추가
            left_x, right_x = copy.deepcopy(x), copy.deepcopy(x)

            if left_x[1] + 1 == n and left_x[2] == n and left_x[3] + 1 == 0:
                result.append(left_x[0] + '(')
            else:
                if left_x[1] + 1 <= n and left_x[2] <= n and (0 <= left_x[3] + 1 <= n):
                    s.append([x[0] + '(', left_x[1] + 1, left_x[2], left_x[3] + 1])
            # ')' 추가
            if right_x[1] == n and right_x[2] + 1 == n and right_x[3] - 1 == 0:
                result.append(right_x[0] + ')')
            else:
                if right_x[1] <= n and right_x[2] + 1 <= n and (0 <= right_x[3] - 1 <= n):
                    s.append([right_x[0] + ')', right_x[1], right_x[2] + 1, right_x[3] - 1])

        return result