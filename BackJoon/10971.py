def dfs(start, current, sum):
    global min_cost, visit, matrix, n

    # min_cost보다 sum의 값이 크면 더 계산하지 않는다.
    if sum >= min_cost:
        return

    # 시작점과 최근 탐색 노드가 같고, 모든 노드를 방문한 상태인 경우 최소 비용을 비교한다.
    if start == current and all(visit):
        min_cost = min(sum, min_cost)

    else:
        for i in range(n):
            if not visit[i] and matrix[current][i] != 0:
                visit[i] = True
                dfs(start, i, sum + matrix[current][i])
                visit[i] = False


def solution(N, arr):
    global min_cost, visit, matrix, n
    matrix = arr
    n = N
    # 최소 비용 초기화
    min_cost = 10 ** 7
    visit = [False for _ in range(n)]
    dfs(0, 0, 0)
    print(min_cost)


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    solution(N, arr)
