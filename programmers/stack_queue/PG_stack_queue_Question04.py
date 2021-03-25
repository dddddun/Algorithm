
from collections import deque
def solution(priorities, location):
    dq = deque()
    for p in priorities:
        dq.append([p, 0])
    dq[location][1] = 1

    cnt = 0
    while dq:
        x = dq.popleft()
        cnt += 1
        if dq:
            if x[0] >= max(d[0] for d in dq):
                if x[1] == 1:
                    break
            else:
                dq.append(x)
                cnt -= 1
    return cnt
'''

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''
solution([1, 1, 9, 1, 1, 1], 0)