def dfs(L, sum, numbers, target):
    global cnt
    if L == len(numbers):
        if sum == target:
            cnt += 1
    else:
        dfs(L+1, sum + numbers[L], numbers, target)
        dfs(L+1, sum - numbers[L], numbers, target)


def solution(n, t):
    global cnt
    cnt = 0
    answer = 0
    numbers, target = n, t
    dfs(0, 0, numbers, target)
    l = [(x, -x) for x in numbers]
    print(l)
    # print(cnt)
    return answer


solution([1, 1, 1, 1, 1], 3)


