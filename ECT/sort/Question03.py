import heapq

def solution(n, cards):
    q = []
    for card in cards:
        heapq.heappush(q, card)
    answer = 0
    while len(q) != 1:
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        answer += first + second
        heapq.heappush(q, first + second)
    print(answer)


solution(3, [10, 20, 40])