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




solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
