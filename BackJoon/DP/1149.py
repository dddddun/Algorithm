def solution(n, dp):
    for i in range(1, n):
        # 0:R, 1:G, 2:B
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]
    print(min(dp[n-1]))


if __name__ == "__main__":
    n = int(input())
    cost = list()
    for _ in range(n):
        cost.append(list(map(int, input().split())))
    solution(n, cost)




# 3 (집의 수)
# 26 40 83 (칠 비용)
# 49 60 57
# 13 89 99

