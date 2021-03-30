import heapq

def heapsort_max(iter):
    heap = []
    max_heap = []
    for value in iter:
        heapq.heappush(heap, -value)
    for _ in range(len(heap)):
        max_heap.append(-heapq.heappop(heap))
    return max_heap

def heapsort_min(iter):
    heap = []
    for value in iter:
        heapq.heappush(heap, value)
    return heap

def solution(oper):
    answer = []
    operations = []
    q = []
    for x in oper:
        operations.append(x.split())

    for string, integer in operations:
        # 주어진 숫자 삽입
        if string == "I":
            q.append(int(integer))

        if string == "D" and len(q) != 0:
            # 최댓값 삭제
            if integer == "1":
                q = heapsort_max(q)
                heapq.heappop(q)
            # 최솟값 삭제
            else:
                q = heapsort_min(q)
                heapq.heappop(q)

    if len(q) == 0:
        return [0, 0]
    else:
        answer.append(heapq.heappop(heapsort_max(q)))
        answer.append(heapq.heappop(heapsort_min(q)))
        return answer


solution(["I 7","I 5","I -5","D -1"])