# 스택을 사용해 풀이
'''
def solution(tickets):
    routes = dict()
    for start, end in tickets:
        routes[start] = routes.get(start, []) + [end]
    for route in routes:
        routes[route].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        start = stack[-1]
        if start not in routes or len(routes[start]) == 0:
            path.append(stack.pop())

        else:
            stack.append(routes[start][-1])
            routes[start] = routes[start][:-1]

    answer = path[::-1]
    # print(answer)
    return answer
'''


# 재귀함수를 사용해 풀이
def dfs(graph, N, start, path):
    path.append(start)
    if len(path) == N + 1:
        return True
    if start not in graph:
        path.pop()
        return False

    for i in range(len(graph[start])):
        end = graph[start][-1]
        graph[start].pop()

        if dfs(graph, N, end, path):
            return True

        graph[start].insert(0, end)

    path.pop()
    return False


def solution(tickets):
    answer = []
    routes = dict()
    for start, end in tickets:
        routes[start] = routes.get(start, []) + [end]
    for route in routes:
        routes[route].sort(reverse=True)

    N = len(tickets)
    path = []

    if dfs(routes, N, "ICN", path):
        answer = path
    print(answer)
    return answer



solution([["ICN", "B"], ["ICN", "A"], ["A", "C"], ["B", "ICN"]])