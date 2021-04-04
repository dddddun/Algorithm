# DFS
'''
def solution(n, computers):
    ch = [False] * n
    answer = 0

    def dfs(x):
        if ch[x]:
            return
        else:
            ch[x] = True
            for i in range(n):
                if not ch[i] and computers[x][i] == 1:
                    dfs(i)

    while True:
        if False in ch:
            dfs(ch.index(False))
            answer += 1
        else:
            break
    return answer
'''
from collections import deque
def solution(n, computers):
    answer = 0
    ch = [False] * n
    # ch = [False for i in range(n)] 위의 코드와 같은 의미

    def bfs(x):
        q = deque()
        q.append(x)
        while q:
            tmp = q.popleft()
            ch[tmp] = True
            for i in range(n):
                if not ch[i] and tmp != i and computers[tmp][i] == 1:
                    q.append(i)

    while True:
        if False in ch:
            bfs(ch.index(False))
            answer += 1
        else:
            break
    print(answer)
    return answer




solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
