# 나의 풀이
from collections import deque
def solution(progresses, speeds):
    answer = []
    tmp = deque()
    for p, s in zip(progresses, speeds):
        if (100-p) % s != 0:
            tmp.append((100 - p) // s + 1)
        else:
            tmp.append((100-p) // s)

    while tmp:
        cnt = 1
        x = tmp.popleft()
        if len(tmp) == 0:
            answer.append(cnt)
            break
        while tmp and x >= tmp[0]:
            cnt += 1
            tmp.popleft()
        answer.append(cnt)
    return answer


# 해설
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])