# 나의 풀이 (실패)
'''
from collections import deque


def solution(begin, target, words):
    global answer
    answer = 0
    dic = dict.fromkeys(words, False)
    dic[begin] = False

    def bfs(w):
        global answer
        q = deque()
        q.append(w)
        while q:
            tmp = q.popleft()
            for word in words:
                cnt = 0
                if not dic[word]:
                    for w in word:
                        if w in tmp:
                            cnt += 1
                    if cnt == 3:
                        answer += 1
                        return answer
                    if cnt == 2:
                        dic[word] = True
                        answer += 1
                        q.append(word)
        else:
            return 0

    if target not in dic:
        return 0
    else:
        bfs(begin)
    print(answer)

    return answer
'''

# 해설 참고

from collections import deque


def get_adjacent(current, words):
    for word in words:
        if sum([(1 if x != y else 0) for x, y in zip(current, word)]) == 1:
            #print(current, word)
            yield word


def solution(begin, target, words):
    dic = {begin: 0}
    queue = deque([begin])
    while queue:
        current = queue.popleft()
        for next_word in get_adjacent(current, words):
            if next_word not in dic:
                dic[next_word] = dic[current] + 1
                queue.append(next_word)

    # print(dic)
    # print(dic.get(target, 0))
    return dic.get(target, 0)


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
