def permutaion(level, start):
    global n, m, arr, res, ch
    if level == m:
        print(' '.join(map(str, res)))
    else:
        for i in range(start, n):
            if not ch[i]:
                ch[i] = True
                res.append(arr[i])
                permutaion(level + 1, i + 1)
                res.pop()
                ch[i] = False


def solution(N, M):
    global n, m, arr, res, ch
    n, m = N, M
    arr = [i for i in range(1, n + 1)]
    ch = [False for _ in range(n)]
    res = list()
    permutaion(0, 0)


if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)