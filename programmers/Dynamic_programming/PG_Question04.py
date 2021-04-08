def solution(money):
    N = len(money)

    # 첫 번째 집을 터는 경우 (마지막 집은 못 턴다)
    # 마지막 집을 털 수 없으므로 탐색 범위가 N - 1 이다.
    # 두 번째 집을 털 수 없으므로 두 번째 집의 값을 첫 번째 집의 값으로 초기화 한다.
    dq = [0] * (N-1)
    dq[0], dq[1] = money[0], money[0]
    for i in range(2, N-1):
        dq[i] = max(money[i]+dq[i-2], dq[i-1])

    # 첫 번째 집을 털지 않는 경우 (마지막 집을 털 수 있다)
    # 첫 번째 집을 털 수 없으므로 0으로 초기화 한다.
    _dq = [0] * N
    _dq[1] = money[1]
    for i in range(2, N):
        _dq[i] = max(money[i]+_dq[i-2], _dq[i-1])

    return max(max(dq), max(_dq))


# solution([1, 2, 3, 1])