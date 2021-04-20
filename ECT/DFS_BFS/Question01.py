from collections import deque


def bfs(roads, start, visited):
    q = deque([start])
    visited[start] = 0
    while q:
        current = q.popleft()
        for next_node in roads[current]:
            if visited[next_node] == -1:
                q.append(next_node)
                visited[next_node] = visited[current] + 1


def solution(n, m, k, x, r):
    visited = [-1] * (n + 1)
    roads = [[] for _ in range(n + 1)]

    for start, end in r:
        roads[start].append(end)

    bfs(roads, x, visited)

    if k not in visited:
        print(-1)
        return

    for i, node in enumerate(visited):
        if node == k:
            print(i, end=' ')


# solution(4, 4, 2, 1, [[1, 2], [1, 3], [2, 3], [2, 4]])
# solution(4, 3, 2, 1, [[1, 2], [1, 3], [1, 4]])
solution(4, 4, 1, 1, [[1, 2], [1, 3], [2, 3], [2, 4]])