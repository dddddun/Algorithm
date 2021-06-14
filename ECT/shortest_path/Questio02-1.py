import heapq


def solution(n, m, array):
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    for s, e in array:
        graph[s].append((e, 1))
        graph[e].append((s, 1))
    distance = [INF] * (n + 1)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0,start))
        distance[start] = 0
        while q:
            dist, current = heapq.heappop(q)
            if distance[current] < dist:

            for next_node, next_dist in graph[current]:
                cost = dist + next_dist
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(cost, next_node)
    dijkstra(1)







solution(6, 7, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
