import heapq


def solution(n, m, start, roads):
    INF = int(1e9)
    graph = [[] for i in range(n + 1)]
    for start, end, dist in roads:
        graph[start].append((end, dist))
    distance = [INF] * (n + 1)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for _end, _dist in graph[now]:
                cost = dist + _dist
                if distance[_end] > cost:
                    distance[_end] = cost
                    heapq.heappush(q, (cost, _end))

    dijkstra(start)

    cities, max_distance = -1, 0
    for d in distance:
        if d != INF:
            cities += 1
            max_distance = max(max_distance, d)

    return cities, max_distance



solution(3, 2, 1, [[1, 2, 4], [1, 3, 2]])
