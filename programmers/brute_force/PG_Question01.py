# 나의 풀이
'''
def solution(answers):
    answer = []
    _answer = []
    supo = ['12345', '21232425', '21232425']
    supo_ans = []
    answers_cnt = len(answers)
    top = 0
    for pattern in supo:
        a = answers_cnt // len(pattern)
        b = answers_cnt % len(pattern)
        supo_ans.append(pattern * a + pattern[0:b])

    for i in range(3):
        cnt = 0
        for j in range(answers_cnt):
            if int(supo_ans[i][j]) == int(answers[j]):
                cnt += 1
        _answer.append([i+1, cnt])

    _answer.sort(reverse=True, key=lambda x: [x[1], x[0]])

    if _answer[0][1] == _answer[1][1] != _answer[2][1]:
        del _answer[2]
    elif _answer[0][1] != _answer[1][1]:
        del _answer[2]
        del _answer[1]

    for x, y in _answer:
        answer.append(x)

    return answer


print(solution([1,2,3,4,5]))
'''



# 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
