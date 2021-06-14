def solution(n, m, buses):
    INF = int(1e9)
    dp = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0

    for a, b, c in buses:
        if dp[a][b] > c:
            dp[a][b] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    for a in range(1, n+1):
        for b in range(1, n+1):
            if dp[a][b] == INF:
                print(0, end=" ")
            else:
                print(dp[a][b], end=" ")
        print()




solution(5, 14, [[1, 2, 2], [1, 3, 3], [1, 4, 1], [1, 5, 10], [2, 4, 2], [3, 4, 1], [3, 5, 1], [4, 5, 3], [3, 5, 10], [3, 1, 8], [1, 4, 2], [5, 1, 7], [3, 4, 2], [5, 2, 4]])