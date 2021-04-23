def solution(n, m, g):
    dp = [[0] * m for _ in range(n)]
    for i in range(n * m):
        dp[i // m][i % m] = g[i]

    # 열을 고정하고 행별로 값을 비교한다.
    for j in range(1, m):
        for i in range(n):

            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]

            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            # 세가지 경우의 수 중 가장 큰 값을 더한다.
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    answer = 0
    # m - 1 열에 있는 값들 중 가장 큰 값이 answer
    for i in range(n):
        answer = max(answer, dp[i][m - 1])

    return answer


solution(3, 4, [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7])