from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        # 현재 위치를 기준으로 위, 오른쪽, 아래, 왼쪽 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖이면 다음 루프
            if nx < 0 or nx >= n or ny > 0 or ny >= m:
                continue
            # 범위 안에 있지만 해당 값이 0 이면
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))
    return graph[n - 1][m - 1]


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

bfs(0, 0)
