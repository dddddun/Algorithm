def solution(n, lost, reserve):
    for i in range(1, n+1):
        if i in lost:
            if i - 1 in reserve:
                reserve.pop(reserve.index(i - 1))
                lost.pop(lost.index(i))
            elif i + 1 in reserve:
                reserve.pop(reserve.index(i + 1))
                lost.pop(lost.index(i))
    print(n - len(lost))
    return n - len(lost)


solution(5, [2, 4], [1, 3, 5])