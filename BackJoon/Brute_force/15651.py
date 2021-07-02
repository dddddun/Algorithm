def permutaion(level):
    global n, m, arr, res, ch
    if level == m:
        print(' '.join(map(str, res)))
    else:
        for i in range(n):
            res.append(arr[i])
            permutaion(level + 1)
            res.pop()


def solution(N, M):
    global n, m, arr, res, ch
    n, m = N, M
    arr = [i for i in range(1, n + 1)]
    res = list()
    permutaion(0)


if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)