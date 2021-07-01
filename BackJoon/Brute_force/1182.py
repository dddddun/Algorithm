def dfs(level, sum):
    global n, s, cnt, arr
    if level == n:
        if sum == s:
            cnt += 1
    else:
        dfs(level + 1, sum + arr[level])
        dfs(level + 1, sum)


def solution(N, S, array):
    global n, s, cnt, arr
    # 정수의 개수
    n = N
    # 문제에서 원하는 수열의 합
    s = S
    arr = array
    cnt = 0
    dfs(0, 0)

    # s가 0일 경우 부분수열 중 공집합인 부분수열을 cnt에서 제외한다.
    if s == 0:
        print(cnt - 1)
    else:
        print(cnt)


if __name__ == "__main__":
    N, S = map(int, input().split())
    array = list(map(int, input().split()))
    solution(N, S, array)