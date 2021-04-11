# 나의 풀이 (실패)
'''
from collections import deque
def solution(n, edge):
    graph = dict()
    for start, end in edge:
        graph[start] = graph.get(start, []) + [end]
    dq = deque()
    dq.append(1)
    cnt = 0
    while dq:
        current = dq.popleft()
        if current in graph and len(graph[current]) != 0:
            dq.append(graph[current].pop())
            cnt += 1
    print(cnt)'''


# 풀이 참고
'''
from collections import defaultdict


def bfs(graph, start, distances):
    q = [start]
    visited = set([start])

    while len(q) > 0:
        current = q.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                distances[neighbor] = distances[current] + 1

def solution(n, edge):
    # 그래프 만들기
    graph = defaultdict(list)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # bfs 탐색 (최단 거리를 구해야 하므로.)
    distances = [0]*(n+1)
    bfs(graph, 1, distances)

    max_distance = max(distances)
    answer = 0

    for distance in distances:
        if distance == max_distance:
            answer += 1

    return answer
'''



from collections import deque, Counter


def solution(n, edge):
    edges = dict()

    # 양방향 그래프 이므로 start, end를 뒤집은 값도 담는다.
    for start, end in edge:
        edges[start] = edges.get(start, []) + [end]
        edges[end] = edges.get(end, []) + [start]

    # 노드 1로부터 떨어진 거리를 담는 리스트를 만든다.
    ch = [0] * (n+1)

    # 노드 1부터 BFS 순회를 하며, 연결된 노드들을 순차적으로 탐색한다.
    stack = deque([1])
    distance = 0
    while stack:
        # 현재 스택에 담겨있는 만큼(같은 거리의 노드들)만 pop한다.
        size = len(stack)
        for i in range(size):
            current = stack.popleft()

            # 방문하지 않은 경우(0인 경우) 거리를 입력하고,
            # 그 노드와 연결된 모든 노드들을 큐에 담는다.
            if ch[current] == 0:
                ch[current] = distance
                for next_num in edges[current]:
                    stack.append(next_num)
        distance += 1

    # 노드 1에서 노드 1로 오는 값은 삭제(0)한다.
    ch[1] = 0

    # 거리가 가장 긴 값의 개수를 반환한다.
    max_dist = max(ch)
    # print(Counter(ch)[max_dist])
    return Counter(ch)[max_dist]



solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])