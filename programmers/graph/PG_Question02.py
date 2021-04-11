# set()을 사용한 풀이
'''
def solution(n, results):
    lower = [set() for _ in range(n+1)]
    upper = [set() for _ in range(n+1)]

    for [winner, loser] in results:
        upper[loser].add(winner)
        lower[winner].add(loser)
    print(upper)
    print(lower)

    for i in range(1, n+1):
        for low in lower[i]:
            upper[low].update(upper[i])
        for up in upper[i]:
            lower[up].update(lower[i])

    answer = 0
    for i in range(1, n+1):
        if len(upper[i]) + len(lower[i]) == n - 1:
            answer += 1
    print(answer)
'''

# 플로이드 와샬 알고리즘을 사용한 풀이
from collections import Counter


def solution(n, results):
    # p1이 p2를 이겼을 때는 1, 졌을 때는 -1
    board = [[0] * n for _ in range(n)]
    for p1, p2 in results:
        board[p1-1][p2-1] = 1
        board[p2-1][p1-1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    if board[i][k] == 1 and board[k][j] == 1:
                        board[i][j] = 1
                    elif board[i][k] == -1 and board[k][j] == -1:
                        board[i][j] = -1
    answer = 0
    for i in range(n):
        if Counter(board[i])[0] == 1:
            answer += 1

    return answer




solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])