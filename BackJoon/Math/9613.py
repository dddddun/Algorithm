t = int(input())

# 최대공약수 구하기 (재귀함수)
def mcd(x, y):
    if y == 0:
        return x
    else:
        return mcd(y, x % y)


for _ in range(t):
    answer = 0
    t_case = list(map(int, input().split()))
    t_case_len = t_case[0]
    t_case = t_case[1:]
    for i in range(t_case_len):
        for j in range(i + 1, t_case_len):
            if t_case[i] >= t_case[j]:
                answer += mcd(t_case[i], t_case[j])
            else:
                answer += mcd(t_case[j], t_case[i])
    print(answer)
