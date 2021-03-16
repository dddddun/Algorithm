# 나의 풀이 1
'''
def solution(people, limit):
    people.sort()
    left_point = 0
    right_point = len(people)-1
    cnt = 0
    answer = 0
    while True:
        if left_point > right_point:
            break
        if left_point == right_point:
            cnt += 1
            break
        if people[left_point] + people[right_point] > limit:
            right_point -= 1
            cnt += 1
        else:
            left_point += 1
            right_point -= 1
            cnt += 1
    answer = cnt
    return answer
print(solution([70, 80, 50], 100))
'''

# 풀이
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
