# 나의 풀이
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] < K and len(scoville) > 1:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first+second*2)
            answer += 1
        else:
            if scoville[0] > K:
                break
            else:
                answer = -1
                break
    return answer

# 풀이
'''
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
'''

solution([1, 2, 3, 9, 10, 12], 7)