def dfs(level, start):
    global n, rotto, permutation
    if level == 6:
        for per in permutation:
            print(per, end=' ')
        print()
    else:
        for i in range(start, n):
            permutation[level] = rotto[i]
            dfs(level + 1, i + 1)


def solution(N, rotto_arr):
    global n, rotto, permutation
    n = N
    rotto = rotto_arr
    permutation = [0] * 6
    dfs(0, 0)
    print()


if __name__ == "__main__":
    while True:
        rotto_arr = list(map(int, input().split()))
        if rotto_arr[0] == 0: break
        N = rotto_arr[0]
        rotto_arr = rotto_arr[1:]
        solution(N, rotto_arr)