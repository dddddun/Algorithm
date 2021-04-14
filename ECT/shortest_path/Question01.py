def solution(n, m, companies, x, k):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                graph[i][j] = 0

    # 간선에 대한 가중치는 1로 초기화 (무방향 그래프이므로 시작, 끝 값 바꾼 경우도 초기화)
    for start, end in companies:
        graph[start][end] = 1
        graph[end][start] = 1

    # 플로이드 워셜 알고리즘 적용
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 도달할 수 없는 경우 -1 리턴
    if graph[1][k] == INF or graph[k][x] == INF:
        return -1

    return graph[1][k] + graph[k][x]


# solution(5, 7, [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [4, 5]], 4, 5)