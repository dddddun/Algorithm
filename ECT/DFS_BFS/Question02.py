from itertools import combinations
from collections import deque
import copy


def cnt_safe(arr, cnt):
    n = len(arr)
    m = len(arr[0])
    for i in range(n * m):
        if arr[i // m][i % m] == 0:
            cnt += 1
    return cnt


def bfs(arr, virus):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for v in virus:
        q = deque([v])
        while q:
            x, y = q.popleft()
            for i in range(4):
                _x, _y = x + dx[i], y + dy[i]
                if 0 <= _x < len(arr) and 0 <= _y < len(arr[0]) and arr[_x][_y] == 0:
                    arr[_x][_y] = 2
                    q.append([_x, _y])
    return arr



def solution(n, m, maps):
    virus = []
    zero = []
    max_safe = 0
    for i in range(n * m):
        if maps[i // m][i % m] == 0:
            zero.append([i // m, i % m])
        elif maps[i // m][i % m] == 2:
            virus.append([i // m, i % m])

    # 벽 3개 세우기 (조합)
    result = list(combinations(zero, 3))

    for k in range(len(result)):
        temp_arr = copy.deepcopy(maps)
        for i in range(3):
            # 벽 세우기
            temp_arr[result[k][i][0]][result[k][i][1]] = 1

        # 바이러스 전파
        virus_area = bfs(temp_arr, virus)

        # 안전구역 count
        cnt = cnt_safe(virus_area, 0)
        max_safe = max(max_safe, cnt)

    return max_safe



solution(7, 7, [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]])
