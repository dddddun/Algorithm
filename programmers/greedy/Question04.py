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