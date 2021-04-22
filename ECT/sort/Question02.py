import heapq

def solution(N, stages):
    fail = []
    for i in range(1, N + 1):
        cnt = 0
        candidate = 0
        for stage in stages:
            if i - 1 < stage <= i:
                cnt += 1
            if stage >= i:
                candidate += 1

        if candidate == 0:
            heapq.heappush(fail, (0, 0, i))
        else:
            _fail = cnt / candidate
            heapq.heappush(fail, (-(_fail), _fail, i))
    answer = []
    for _ in range(N):
        answer.append(heapq.heappop(fail)[2])

    print(answer)
    return answer

solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])

