# 처음 풀이
'''
def solution(n, edge):
    dic = dict()
    for start, end in edge:
        dic[start] = dic.get(start, []) + [end]

    stack = [1]
    while stack:
        tmp = stack.pop(0)
        for i in dic[tmp]:
            # if len(dic[tmp]) != 0:
            stack.append(dic[tmp][-1])

    print(dic)
'''

from collections import deque


def solution(n, edge):
    routes = dict()
    for e1, e2 in edge:
        routes.setdefault(e1, []).append(e2)
        routes.setdefault(e2, []).append(e1)

    q = deque([[1, 0]])  # node number, depth
    check = [-1] * (n + 1)
    while q:
        index, depth = q.popleft()
        check[index] = depth
        for i in routes[index]:
            if check[i] == -1:
                check[i] = 0
                q.append([i, depth + 1])
        depth += 1
    return check.count(max(check))

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])