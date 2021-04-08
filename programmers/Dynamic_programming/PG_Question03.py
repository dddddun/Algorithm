# 나의 풀이 (완전 틀림)
'''
def solution(m, n, puddles):
    dq = [[0]*m for _ in range(n)]
    dq[0][0] = 1
    dx = [0, 1]
    dy = [1, 0]
    for puddle_x, puddle_y in puddles:
        dq[puddle_x-1][puddle_y-1] = 1
    queue = [[0, 0]]
    max = []
    while queue:
        x, y = queue.pop(0)
        for i in range(2):
            _x, _y = x+dx[i], y+dy[i]
            if 0 <= _x < n and 0 <= _y < m:
                if dq[_x][_y] == 0:
                    dq[_x][_y] = dq[x][y] + 1
                    queue.append([_x, _y])
                if _x == n-1 and _y == m-1:
                    max.append(dq[_x][_y])
    return dq[n-1][m-1] - 2
'''
def solution(m, n, puddles):
    dq = [[0] * (m+1) for _ in range(n+1)]
    dq[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 첫 칸
            if i == j == 1:
                continue

            # 웅덩이인 경우
            if [j, i] in puddles:
                dq[i][j] = 0

            # 점화식
            # 도착 지점으로의 경로 개수 = 왼쪽 루트 개수 + 윗쪽 루트 개수
            # 오른쪽, 아래 방향으로만 움직일 수 있으므로 특정 지점까지의 거리는 항상 최단거리이다.
            else:
                dq[i][j] = dq[i-1][j] + dq[i][j-1]
    # print(dq)
    return dq[n][m] % 1000000007


solution(4, 3, [[2, 2]])