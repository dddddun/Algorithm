def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1
print(cnt)














'''
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def DFS(x, y):
    # 종료 조건
    if x <= 1 or x >= n or y <= -1 or y >= m:
        return False
    # DFS로 노드를 방문하고 연결된 모든 노드들도 방문
    if graph[x][y] == 0:
        graph[x][y] = 1
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True


result = 0

for i in range(n):
    for j in range(m):
        if DFS(i, j):
            result += 1
print(result)
'''