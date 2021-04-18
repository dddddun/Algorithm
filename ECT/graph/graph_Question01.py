def find_parent(parent, teams, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, teams, parent[x])
    return parent[x]


def union_parent(parent, teams, a, b):
    a = find_parent(parent, teams, a)
    b = find_parent(parent, teams, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    elif a == b:
        return


def is_team(parent, teams, a, b):
    a = find_parent(parent, teams, a)
    b = find_parent(parent, teams, b)
    if a == b:
        print("YES")
    else:
        print("NO")


def solution(n, m, teams):
    parent = [[] for _ in range(n+1)]
    for i in range(n + 1):
        parent[i] = i

    for oper, a, b in teams:
        if oper == 0:
            union_parent(parent, teams, a, b)
        elif oper == 1:
            is_team(parent, teams, a, b)





solution(7, 8, [[0, 1, 3], [1, 1, 7], [0, 7, 6], [1, 7, 1], [0, 3, 7], [0, 4, 2], [0, 1, 1], [1, 1, 1]])