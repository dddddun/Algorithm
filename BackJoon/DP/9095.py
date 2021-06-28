def count_solution(i, dp):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]


def solution(T, n_list):
    # dq 초기화
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 12):
        count_solution(i, dp)

    for n in n_list:
        print(dp[n])


if __name__ == "__main__":
    T = int(input())
    n_list = []
    for _ in range(T):
        n_list.append(int(input()))
    solution(T, n_list)
