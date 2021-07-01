def dfs(level, res, add, sub, mul, div):
    global n, numbers, _max, _min
    if level == n:
        _max = max(_max, res)
        _min = min(_min, res)
        return
    else:
        if add:
            dfs(level + 1, res + numbers[level], add - 1, sub, mul, div)
        if sub:
            dfs(level + 1, res - numbers[level], add, sub - 1, mul, div)
        if mul:
            dfs(level + 1, res * numbers[level], add, sub, mul - 1, div)
        if div:
            dfs(level + 1, int(res / numbers[level]), add, sub, mul, div - 1)


def solution(N, num, operater):
    global n, numbers, _max, _min
    n = N
    numbers = num
    add, sub, mul, div = operater
    _max = -1e9
    _min = 1e9
    dfs(1, numbers[0], add, sub, mul, div)
    print(_max)
    print(_min)


if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().split()))
    operater = list(map(int, input().split()))
    solution(N, num, operater)