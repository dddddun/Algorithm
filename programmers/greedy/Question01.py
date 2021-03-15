# 체육복 문제

def solution(n, lost, reserve):
    answer = 0
    ch = [1] * (n)
    ch.insert(0, 0)
    ch.append(0)
    for i in lost:
        ch[i] -= 1
    for j in reserve:
        ch[j] += 1

    for x in lost:
        if ch[x] == 0 and ch[x - 1] == 2:
            ch[x - 1] -= 1
            ch[x] += 1
        elif ch[x] == 0 and ch[x + 1] == 2:
            ch[x + 1] -= 1
            ch[x] += 1

    answer = n - ch.count(0) + 2

    return answer