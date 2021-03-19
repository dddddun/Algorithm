# 순열을 구하는 로직이 틀렸다.... (16.7점 나옴)
'''
def DFS(L):
    if L == n:
        if sum(ch) == 0:
            return
        str = ''
        for j in range(n):
            if ch[j] == 1:
                str += num[j]
        res.add(int(str))
        return

    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0
                DFS(L+1)

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    global n, ch, res, num
    num = numbers
    n = len(numbers)
    ch = [0] * n
    res = set()
    answer = 0
    DFS(0)
    res = list(res)
    print(res)
    for x in res:
        if isPrime(x):
            answer += 1
    print(answer)
    return answer
'''

import math
from itertools import permutations


def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True


def solution(numbers):
    answer = []
    cnt = 0
    for i in range(1, len(numbers)+1):
        nums = list(permutations(numbers, i))
        for j in nums:
            print(j)
            # num = int(''.join(map(str,arr[j])))
            num = int(''.join(j))
            if is_prime(num):
                answer.append(num)
    answer = list(set(answer))
    print(answer)
    return len(answer)

solution("011")
