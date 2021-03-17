# 나의 풀이
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    v1 = find(x)
    v2 = find(y)
    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2


def solution(n, costs):
    global parent
    answer = 0
    parent = list(range(n))
    costs.sort(key=lambda x: [x[2], x[0], x[1]])
    for cost in costs:
        a, b, t = cost
        if find(a) != find(b):
            union(a, b)
            answer += t
    return answer

# 해설
'''
def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)

def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer
'''
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

