def solution(n, dp):

    for i in range(1, n):
        for j in range(len(dp[i])):
            # 왼쪽 위에서 내려오는 경우
            if j == 0:
                left = 0
            else:
                left = dp[i - 1][j - 1]

            # 오른쪽 위에서 내려오는 경우
            if j == len(dp[i]) - 1:
                right = 0
            else:
                right = dp[i - 1][j]

            dp[i][j] = dp[i][j] + max(left, right)

    return max(dp[n-1])


solution(5, [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])