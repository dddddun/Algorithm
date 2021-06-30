# 비밀번호 조합을 구하는 함수
def dfs(level, start, tmp_res):
    global l, c, character, results
    if level == l:
        results.append(''.join(map(str, tmp_res)))
    else:
        for i in range(start, c):
            tmp_res[level] = character[i]
            dfs(level + 1, i + 1, tmp_res)


# 비밀번호 조합에서 모음이 1개 이상이고, 자음이 2개 이상인지 체크하는 함수
def password(results):
    for result in results:
        cnt_vowel = 0
        cnt_consonant = 0
        for char in result:
            if char in 'aeiou':
                cnt_vowel += 1
            else:
                cnt_consonant += 1
        if cnt_vowel >= 1 and cnt_consonant >= 2:
            print(result)


def solution(L, C, arr):
    global l, c, character, results
    l, c = L, C
    character = sorted(arr)
    tmp_res = ['' for _ in range(l)]
    results = []
    dfs(0, 0, tmp_res)
    password(results)


if __name__ == "__main__":
    L, C = map(int, input().split())
    arr = list(input().split())
    solution(L, C, arr)