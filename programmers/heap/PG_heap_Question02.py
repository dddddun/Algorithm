import heapq
def solution(jobs):
    answer, start, end = 0, 0, 0
    hq = []
    jobs.sort(key=lambda x: (x[0], x[1]))
    print(jobs)
    now = jobs.pop(0)
    end = now[0] + now[1]
    for job in jobs:
        if job[0] <= end:
            heapq.heappush(hq, job)
    now = heapq.heappop(hq)
    end = now[1]


    return answer


solution([[0, 3], [3, 6], [1, 9], [4, 8], [2, 6]])