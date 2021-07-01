def max_revenue():
    global n, time, price, dq
    for i in range(n - 1, -1, -1):
        if time[i] + i <= n:
            dp[i] = max(price[i] + dp[i + time[i]], dp[i + 1])
        else:
            dp[i] = dp[i + 1]



def solution(N, T, P):
    global n, time, price, dp
    n, time, price = N, T, P
    dp = [0 for _ in range(n + 1)]
    max_revenue()
    print(dp[0])



if __name__ == "__main__":
    N = int(input())
    T = [0 for _ in range(N)]
    P = [0 for _ in range(N)]
    for i in range(N):
        t, p = map(int, input().split())
        T[i] = t
        P[i] = p
    solution(N, T, P)