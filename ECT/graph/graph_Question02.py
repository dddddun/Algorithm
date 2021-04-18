def find_parent(parent, roads, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, roads, parent[x])
    return parent[x]


def union_parent(parent, roads, a, b):
    a = find_parent(parent, roads, a)
    b = find_parent(parent, roads, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, m, roads):
    parent = [[] for _ in range(n + 1)]
    for i in range(n + 1):
        parent[i] = i
    result = 0
    roads = sorted(roads, key = lambda x: x[2])
    max_cost = 0
    for a, b, cost in roads:
        if find_parent(parent, roads, a) != find_parent(parent, roads, b):
            union_parent(parent, roads, a, b)
            result += cost
            max_cost = cost

    # 마을은 최소 가중치로만 모두 연결되어있다.
    # 마을을 2로 나누기 위해 길을 하나 제거한다.
    # 제거하는 길은 가장 마지막에 추가된(가중치가 가장 큰) 길이다.
    print(result - max_cost)



solution(7, 12, [[1, 2, 3], [1, 3, 2], [3, 2, 1], [2, 5, 2], [3, 4, 4], [7, 3, 6], [5, 1, 5], [1, 6, 2], [6, 4, 1], [6, 5, 3], [4, 5, 3], [6, 7, 4]])