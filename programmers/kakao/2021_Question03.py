def solution(info, query):
    answer = []
    _info = []
    _query = []
    for i in info:
        _info.append(i.split())

    for q in query:
        _query.append((q.replace(' ' + 'and', '')).split())

    cnt = 0
    for f, g, h, i, j in _query:
        cnt = 0
        for a, b, c, d, e in _info:
            if (f == a or f == '-') and (g == b or g == '-') and (h == c or h == '-') and (i == d or i == '-'):
                if int(j) <= int(e):
                    cnt += 1
        answer.append(cnt)
    print(answer)

    '''inf = dict()
    inf[java], inf[python], inf[cpp] = 0, 1, 2
    jick = dict()
    jick[backend], jick[frontend] = 0, 1
    food = dict()
    food[chicken], food[pizza] = 0, 1'''

    return answer

solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])

def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer







from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []

    # 1. 지원자 정보 parsing
    applicant = defaultdict(list)

    for x in info:
        x = x.split()
        keylist = x[:-1]
        score = int(x[-1])

        # 1-1. 점수를 제외한 4가지 조건이 '-'일수도 있는 16가지 구하기
        for i in range(5):
            for c in combinations(keylist, i):
                key = ''.join(c)

                applicant[key].append(score)

    # 2. applicant의 key에 따른 value 정렬 (점수 정렬)
    for key in applicant.keys():
        applicant[key].sort()

    # 3. 조건 parsing

    for x in query:
        q = []
        x = x.split(' ')

        # 3-1. and, - 제외하기 (필요조건으로만 key생성)
        for y in x:
            if y != 'and' and y != '-':
                q.append(y)

        key = ''.join(q[:-1])
        score = int(q[-1])

        # 3-2. 이분탐색으로 조건에 해당하는 지원자 수 구하기
        count = 0

        if key in applicant.keys():  # 해당 조건의 지원자가 있는지 확인
            value = applicant[key]
            start, end = 0, len(value)
            while start <= end and start < len(value):
                mid = (start + end) // 2

                if value[mid] < score:
                    start = mid + 1
                else:
                    end = mid - 1

            count = len(value) - start

        answer.append(count)

    return answer