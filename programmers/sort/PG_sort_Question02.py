def solution(citations):
    answer = 0
    citations.sort()
    for i in range(1, len(citations)+1):
        cnt = 0
        for x in citations:
            if i <= x:
                cnt += 1
        if i <= cnt:
            answer = i
            break
    # print(answer)
    return answer

solution([3, 0, 6, 1, 5])

# 풀이
'''
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
'''
# 인용 횟수를 정렬하고, 언제 H Index의 최대값을 가지는지 파악합니다.
# 정렬된 인용 횟수에서 i 번째 인용 횟수 citations[i]가 그 인용 횟수 이상의 논문 수인 (전체 논문 수 - i) 보다 크거나 같은 지점에서
# H- Index의 최댓값 (전체 논문 수 - i)가 결정됩니다.
