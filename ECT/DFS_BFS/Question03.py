from itertools import permutations
from collections import deque


# 라이브러리 사용
def solution(n, a, operators):
    operator = []
    for i in range(4):
        for _ in range(operators[i]):
            operator.append(i)
    operand = deque(a)
    tmp_operator = permutations(operator, n - 1)

    max_value = int(-1e9)
    min_value = int(1e9)

    for oper in tmp_operator:
        answer = operand[0]
        for i in range(1, len(operand)):
            if oper[i - 1] == 0:
                answer += operand[i]
            if oper[i - 1] == 1:
                answer -= operand[i]
            if oper[i - 1] == 2:
                answer *= operand[i]
            if oper[i - 1] == 3:
                if answer < 0:
                    answer = -answer
                    answer //= operand[i]
                    answer = -answer
                answer //= operand[i]

        max_value = max(max_value, answer)
        min_value = min(min_value, answer)

    print(max_value, min_value)


# dfs 사용
def dfs(i, now, oper, operand):
    global min_value, max_value, len_oper

    if i == len_oper:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if oper[0] > 0:
            oper[0] -= 1
            dfs(i + 1, now + operand[i], oper, operand)
            oper[0] += 1
        if oper[1] > 0:
            oper[1] -= 1
            dfs(i + 1, now - operand[i], oper, operand)
            oper[1] += 1
        if oper[2] > 0:
            oper[2] -= 1
            dfs(i + 1, now * operand[i], oper, operand)
            oper[2] += 1
        if oper[3] > 0:
            oper[3] -= 1
            dfs(i + 1, int(now / operand[i]), oper, operand)
            oper[3] += 1


def solution(n, a, operators):
    global min_value, max_value, len_oper
    len_oper = n
    min_value = 1e9
    max_value = -1e9
    oper = []
    for i in range(4):
        oper.append(operators[i])

    dfs(1, a[0], oper, a)

    print(max_value, min_value)



solution(3, [3, 4, 5], [1, 0, 1, 0])
# solution(2, [5, 6], [0, 0, 1, 0])
# solution(6, [1, 2, 3, 4, 5, 6], [2, 1, 1, 1])
