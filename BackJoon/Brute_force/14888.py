def dfs(level, res, add, sub, mul, div):
    global operand, n, _max, _min
    if level == n:
        _max = max(res, _max)
        _min = min(res, _min)
    else:
        if add:
            dfs(level + 1, res + operand[level], add - 1, sub, mul, div)
        if sub:
            dfs(level + 1, res - operand[level], add, sub - 1, mul, div)
        if mul:
            dfs(level + 1, res * operand[level], add, sub, mul - 1, div)
        if div:
            dfs(level + 1, int(res / operand[level]), add, sub, mul, div - 1)


def solution(N, opd, opt):
    global operand, n, _max, _min
    n = N
    operand = opd
    add, sub, mul, div = opt
    _max = -1e9
    _min = 1e9
    dfs(1, operand[0], add, sub, mul, div)
    print(_max)
    print(_min)


if __name__ == "__main__":
    N = int(input())
    operand = list(map(int, input().split()))
    operater = map(int, input().split())
    solution(N, operand, operater)


# 접근 방법이 잘못된 나의 풀이
# def operater_permutation_dfs(L, oper, oper_ch, oper_tmp):
#     global operater_permutation
#     if L == len(oper):
#         operater_permutation.append(oper_tmp.copy())
#     else:
#         for i in range(len(oper)):
#             if not oper_ch[i]:
#                 oper_ch[i] = True
#                 oper_tmp.append(oper[i])
#                 operater_permutation_dfs(L + 1, oper, oper_ch, oper_tmp)
#                 oper_ch[i] = False
#                 oper_tmp.pop()
#
#
# def analyze_operater(operater):
#     operater_list = []
#     for i in range(4):
#         for _ in range(operater[i]):
#             if i == 0:
#                 operater_list.append('+')
#             elif i == 1:
#                 operater_list.append('-')
#             elif i == 2:
#                 operater_list.append('*')
#             elif i == 3:
#                 operater_list.append('//')
#     return operater_list
#
#
# def solution(N, opd, opt):
#     global operater_permutation
#     n = N
#     operand = opd
#
#     operater = analyze_operater(opt)
#     operater_ch = [False for _ in range(n - 1)]
#     operater_tmp = []
#     operater_permutation = []
#
#     operater_permutation_dfs(0, operater, operater_ch, operater_tmp)
#
#     print(operater_permutation)
#
#
# if __name__ == "__main__":
#     N = int(input())
#     opd = list(map(int, input().split()))
#     opt = list(map(int, input().split()))
#     solution(N, opd, opt)

