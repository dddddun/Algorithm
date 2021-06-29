def dfs(L, n, arr):
    global max_num, ch, _arr
    if L == n:
        tmp = 0
        for i in range(n - 1):
            tmp += abs(_arr[i] - _arr[i + 1])
        max_num = max(tmp, max_num)
    else:
        for i in range(n):
            if ch[i]:
                ch[i] = False
                _arr.append(arr[i])
                dfs(L + 1, n, arr)
                ch[i] = True
                _arr.pop()


def solution(n, arr):
    global max_num, ch, _arr
    ch = [True] * (n + 1)
    _arr = []
    max_num = 0
    dfs(0, n, arr)
    print(max_num)


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    solution(N, arr)