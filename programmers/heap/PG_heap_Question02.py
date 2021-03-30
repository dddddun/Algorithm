# 나의 풀이 실패
'''
import heapq
def solution(jobs):
    answer = []
    hq = []
    jobs.sort(key=lambda x: (x[0], x[1]))
    first = jobs.pop(0)
    end = first[1]
    hq.append((end, first[0]))
    # 좝스 안에 시작이 끝 보다 작은 애,들을 먼저 뽑아서 hq에 넣는다.
    while jobs:
        print(jobs)
        i = 0
        while max(j[0] for j in jobs) <= end:
            if jobs[i][0] <= end:
                job = jobs.pop(i)
                heapq.heappush(hq, (job[1], job[0]))
            else:
                i += 1

        while hq:
            # 걸리는 시간 = end - start
            hq_job = heapq.heappop(hq)
            end = end + hq_job[0]
            answer.append(end - hq_job[1])
    print(answer)

    return answer
'''


# 해설
from heapq import heappush, heappop


def solution(jobs):
    jobs.sort(reverse=True)
    que = []
    time, total_wait_run, length = 0, 0, len(jobs)
    while jobs or que:
        while jobs and jobs[-1][0] <= time:
            start, running = jobs.pop()
            heappush(que, (running, start))
        if que:
            running, start = heappop(que)
            total_wait_run += time - start + running
            time = time + running
        else:
            time = jobs[-1][0]
    return total_wait_run // length



# solution([[0, 3], [1, 9], [2, 6]])


