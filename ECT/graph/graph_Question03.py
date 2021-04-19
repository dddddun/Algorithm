from collections import deque
import copy

def solution(n, lectures):
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    time = [0] * (n + 1)

    # 간선 정보 입력
    for i, lecture in enumerate(lectures, start=1):
        time[i] = lecture[0]
        for l in lecture[1:-1]:
            # i <- l 이므로 graph[l]값에 i를 append
            graph[l].append(i)
            # i의 진입차수를 1 더해준다
            indegree[i] += 1
    print(graph)
    print(indegree)
    print(time)

    def topology_sort():
        result = copy.deepcopy(time)
        q = deque()

        # 진입 차수가 0인 노드를 큐에 삽입
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
        while q:
            now = q.popleft()
            for next_node in graph[now]:
                result[next_node] = max(result[next_node], time[next_node] + result[now])
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        print(result)

    topology_sort()


solution(5, [[10, -1], [10, 1, -1], [4, 1, -1], [4, 3, 1, -1], [3, 3, -1]])